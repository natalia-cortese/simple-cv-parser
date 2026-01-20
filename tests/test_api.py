from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_parse_resume():
    with open("tests/sample_cv.txt", "rb") as f:
        response = client.post(
            "/parse-resume",
            files={"file": ("cv.txt", f, "text/plain")}
        )

    assert response.status_code == 400

    data = response.json()
    assert "name" not in data
    assert "skills" not in data
