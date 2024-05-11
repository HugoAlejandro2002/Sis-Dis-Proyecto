from os import environ
## LLenar los datos faltantes
## puerto_server = 2024 + mod(codigo_upb,10)
codigo_upb = 62043
puerto_server = 2024 + 62043 % 10
port = int(environ.get("PORT", puerto_server))
host = environ.get("HOST", "localhost")