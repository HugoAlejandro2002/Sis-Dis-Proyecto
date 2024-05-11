import json
import subprocess

# Cargar el archivo JSON con las solicitudes
with open('invalid_request.json', 'r') as file:
    requests = json.load(file)

# Función para enviar solicitudes usando grpcurl
def send_request(data, index):
    # Convierte el diccionario a JSON string y guarda en un archivo temporal
    temp_filename = f'temp_request_{index}.json'
    with open(temp_filename, 'w') as temp_file:
        json.dump(data, temp_file)
    
    # Comando grpcurl
    response = subprocess.run(
        [
            'grpcurl', '-plaintext', '-d', '@', '-import-path', '.', '-proto', 'transporte.proto',
            'localhost:2027', 'Viaje_rpc/Start'
        ],
        stdin=open(temp_filename, 'r'),
        capture_output=True,
        text=True
    )
    
    print(response)
    # Eliminar el archivo temporal después de enviar la solicitud
    subprocess.run(['rm', temp_filename])
    
    return response.stdout

# Iterar sobre cada solicitud y enviarlas
responses = {}
for i, request in enumerate(requests):
    response = send_request(request, i)
    responses[i] = response.strip()  # Usar strip para eliminar espacios en blanco y nuevas líneas
    print(f'Response {i}: {response.strip()}')  # Asegúrate de que la respuesta se muestre correctamente

# Guardar las respuestas en un archivo
with open('responses_log.txt', 'w') as file:
    json.dump(responses, file)

print("Todas las solicitudes han sido enviadas y las respuestas registradas.")
