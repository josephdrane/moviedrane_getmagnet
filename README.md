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
export GCP_PROJECT=<your-gcp-project-id>
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
