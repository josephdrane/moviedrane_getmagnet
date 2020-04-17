# moviedrane_getmagnet
GRPC Service to Get Magnet From IMDB ID

## Dev Environment Setup Steps

- **Setup GRPC and Dockerfile for GCP CloudRun :**
https://github.com/grpc-ecosystem/grpc-cloud-run-example/blob/master/python/README.md

- **Container Registry Setup :** 
https://cloud.google.com/container-registry/docs/pushing-and-pulling 


## Dev Workflow

*Do your code and then*

1. Build Your Docker Image

```bash
cd <project directory>
export GCP_PROJECT=moviedrane-274422
docker build -t gcr.io/$GCP_PROJECT/grpc-moviedrane_getmagnet:latest .
```

2. Update your auth

```bash
gcloud auth login
gcloud auth configure-docker
```

3. Push your Docker Build

```bash
docker push gcr.io/$GCP_PROJECT/grpc-moviedrane_getmagnet:latest
```

4. Deploy to GCP CloudRun

```bash
gcloud run deploy --image gcr.io/$GCP_PROJECT/grpc-moviedrane_getmagnet:latest --platform managed
```

5. Get Endpoint and Test

```bash
ENDPOINT=$(gcloud run services list \
    --project=moviedrane-274422 \
    --region=${GCP_REGION} \
    --platform=managed \
    --format="value(status.address.url)" \
    --filter="metadata.name=grpc-moviedranegetmagnet")

grpcurl \
    -proto magnet.proto \
    -d '{"imdb_id": "tt7146812" }' \
    ${ENDPOINT}:443 \
    Magnet.GetMagnet
```