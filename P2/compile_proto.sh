source ../venv/bin/activate

python3 -m grpc_tools.protoc   -I=./   --python_out=.   --grpc_python_out=.    transporte.proto

echo "Archivos .py y _grpc.py generados correctamente."