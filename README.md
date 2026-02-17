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
