from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_wheat_flow_integration():
    # Full voice->advisory pipeline check
    payload = {
        "text": "aaj barish hogi kya mere gehun ke liye theek hai?",
        "lat": 28.6,
        "lng": 77.2
    }
    response = client.post("/api/v1/advisory", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "gehun" in str(data["aapki_fasal_ke_liye"]["crop"]).lower()
    assert data["namaskar"] is not None
