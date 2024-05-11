def validate_request(request):
    errors = []
    if not request.taxi_id:
        errors.append("taxi_id is required.")
    if not request.conductor_id:
        errors.append("conductor_id is required.")
    if request.tipo_viaje not in [1,2,3]:
        errors.append("tipo_viaje is invalid.")
    if not request.ubicacion or (request.ubicacion.latitud == 0 and request.ubicacion.longitud == 0):
        errors.append("ubicacion is required and must be valid.")
    if not request.tiempo or request.tiempo.seconds == 0:
        errors.append("tiempo is required and must be valid.")

    if errors:
        error_message = "Validation errors: " + ", ".join(errors)
        raise ValueError(error_message)

    return True  # If no errors, validation passes
