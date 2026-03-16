# rest-api-kube

FastAPI hello world with CI (GHCR) and CD (ArgoCD) for Kubernetes.

## Local run

```powershell
python -m venv .venv
. .venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://localhost:8000

## Build container locally

```powershell
docker build -t rest-api-kube:local .
docker run --rm -p 8000:8000 rest-api-kube:local
```

## ArgoCD deploy (Docker Desktop Kubernetes)

Apply the ArgoCD Application:

```powershell
kubectl apply -f argocd/application.yaml
```

The app syncs `k8s/` into the `rest-api-kube` namespace.
