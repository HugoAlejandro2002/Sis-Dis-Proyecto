import taxi_pb2 as pb
import json

def load_json_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

# Cargando los archivos
data_users = load_json_data("sample_request_data.json")

def define_serialized_messages(data_users):
    messages = []
    for i in range(0, len(data_users["taxi_id"])):
        # Iterar por los objetos del archivo .json
        solicitud = pb.TaxiTrip(
            taxi_id=data_users["taxi_id"][f"{i}"],
            conductor_id=data_users["conductor_id"][f"{i}"],
            pasajero_id=data_users["pasajero_id"][f"{i}"].split(","),
            costo_estimado=data_users["costo_estimado"][f"{i}"],
        )
        # Se serializa la solictud
        messages.append(solicitud.SerializeToString())
    return messages

define_serialized_messages(data_users)

messages = define_serialized_messages(data_users)
with open('output_p1b.bin', 'wb') as bin_file:
    for message_bytes in messages:
        bin_file.write(message_bytes)
        
for i in range(10):
    print(messages[i])
        
def plot_messages(data_users):
    import matplotlib.pyplot as plt
    taxi_ids = []
    costos_estimados =[]
    for i in range(0, len(data_users["taxi_id"])):
        # Iterar por los objetos del archivo .json
        taxi_ids.append(data_users["taxi_id"][f"{i}"])
        costos_estimados.append(data_users["costo_estimado"][f"{i}"])
    # Crear gráfica de barras
    plt.figure(figsize=(10, 6))
    plt.bar(taxi_ids, costos_estimados, color='blue')
    plt.xlabel('ID del Taxi')
    plt.ylabel('Costo Estimado ($)')
    plt.title('Costo Estimado por Viaje de Taxi')
    plt.savefig('Costo_Estimado_Taxi.png')
    plt.show()