import taxi_pb2 as pb


solicitud_1 = pb.TaxiTrip(
    taxi_id=55,  
    conductor_id="Sist_dist",
    pasajero_id=["63428", "63438", "63448"],
    costo_estimado=20.50,
)

print("Formato de solicitud:\n", solicitud_1)