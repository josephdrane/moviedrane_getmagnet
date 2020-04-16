# GCP Dockerfile Setup Guide : 
# https://github.com/grpc-ecosystem/grpc-cloud-run-example/blob/master/python/README.md

FROM python:3.8

WORKDIR /srv/grpc

COPY . .

RUN pip install -r requirements.txt && \
    python -m grpc_tools.protoc \
        -I. \
        --python_out=. \
        --grpc_python_out=. \
        magnet.proto

CMD ["python", "server.py"]

