import os
from google.cloud import secretmanager
from app.core.config import settings

def get_secret(secret_id: str) -> str:
    """Fetch secret from Google Secret Manager or Environment."""
    # When deployed via gcloud run --set-secrets, they end up in env
    val = os.getenv(secret_id)
    if val:
        return val
        
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{settings.PROJECT_ID}/secrets/{secret_id}/versions/latest"
    try:
        response = client.access_secret_version(request={"name": name})
        return response.payload.data.decode("UTF-8")
    except Exception:
        # Fallback for local development or missing secrets
        return "mock-secret"
