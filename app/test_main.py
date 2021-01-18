from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_post_sentiment_analysis():
    response = client.post(
        "/sentiment-analysis",
        json={"text": "Bonjour, je suis désespérée, mon enfant ne dort plus"},
    )
    assert response.status_code == 200
