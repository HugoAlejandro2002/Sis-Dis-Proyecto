from concurrent.futures import ThreadPoolExecutor
from grpc_reflection.v1alpha import reflection
import grpc
import log
import uuid
import transporte_pb2 as pb
import transporte_pb2_grpc as rpc
from validation import validate_request

codigo_upb = 62043

def gen_id():
    # el id_gen es un identificador unico
    # se encuentra en formato hex.
    # puede hacer uso de la biblioteca uuid
    id_gen = uuid.uuid4().hex
    return id_gen


class Viaje(rpc.Viaje_rpcServicer):
    def Start(self, request, context):
        # log la solicitud actual
        log.info("viaje: %s", request)

        try:
            validate_request(request)  # Llamada a la función de validación
        except ValueError as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(str(e))
            return pb.StartResponse()
        # generar un nuevo id para el ride
        # obtener este id de la funcion generada anteriormente
        id_viaje = gen_id()
        # obtener el costo estimado del viaje
        costo_base = codigo_upb % 100
        # Calcula el costo en función del tipo de viaje
        if request.tipo_viaje == pb.TipoViaje.POOL:
            # Divide el costo base por el número de pasajeros
            if len(request.pasajero_id) > 0:
                costo_cliente = costo_base / len(request.pasajero_id)
            else:
                costo_cliente = costo_base  # Evita la división por cero
        elif request.tipo_viaje == pb.TipoViaje.PREMIUM:
            # Incrementa el costo base en un 25%
            costo_cliente = costo_base * 1.25
        else:
            # Costo regular si no es ni POOL ni PREMIUM
            costo_cliente = costo_base
        # generar la respuesta en base a la estructura indicada
        # en el .proto file.
        respuesta = pb.StartResponse(viaje_id=id_viaje, costo_cliente=costo_cliente)
        return respuesta


if __name__ == "__main__":
    import config

    # Se crea una nueva instancia de un servidor gRPC
    # Se utiliza un ThreadPoolExecutor para manejar las solicitudes entrantes
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    # Registra un servicio gRPC en un servidor gRPC
    rpc.add_Viaje_rpcServicer_to_server(Viaje(), server)
    names = (
        # adicionar el nombre del servicio
        pb.DESCRIPTOR.services_by_name["Viaje_rpc"].full_name,
        reflection.SERVICE_NAME,
    )
    # Modificación para incluir reflexión
    reflection.enable_server_reflection(names, server)
    addr = f"{config.host}:{config.port}"
    server.add_insecure_port(addr)
    server.start()

    log.info("El servidor esta listo en el puerto %s", addr)
    server.wait_for_termination()