FROM python:3.7.5-slim

WORKDIR /usr/src/app

COPY . .

RUN python3 -m pip install \
        grpcio \
        grpcio-tools
        
EXPOSE 8080

CMD ["python3", "server.py"]

