# CoffeeMart

CoffeeMart is a simple online coffee store application implemented with Flask and prepared for Kubernetes deployment.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://localhost:8080`.

## Build container image

```bash
docker build -t ghcr.io/your-org/coffeemart:latest .
```

## Deploy to Kubernetes

1. Update `image:` in `k8s/deployment.yaml` to your registry/image.
2. Apply manifests:

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml
```

3. Point DNS for `coffeemart.example.com` to your ingress controller (or adjust the host).

## Test

```bash
pip install pytest
pytest
```

## GitHub Actions deployment

This repository includes `.github/workflows/deploy.yml` which will:
- run tests (`pytest`)
- build and push Docker image to GHCR
- deploy to Kubernetes on pushes to `main`

### Required GitHub secrets
- `KUBE_CONFIG`: base64/plain kubeconfig content for the target cluster

Make sure your cluster has an ingress controller (for the provided ingress manifest).
