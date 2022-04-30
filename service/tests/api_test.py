from fastapi.testclient import TestClient

from service.main import app

client = TestClient(app)


def test_vited_search():
    paramss = {
        "search_text": "Pull nike",
        "per_page": 1
    }
    response = client.get("/api/v1/vinted/items", params=paramss)
    assert response.status_code == 200



