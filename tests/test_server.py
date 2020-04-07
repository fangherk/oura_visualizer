import json

import pytest

from backend import batch
from backend.server import app


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_latest_scores(client, monkeypatch):
    mock_response = {
        "sleep": [{"score": 10, "extra_stuff": 232}],
        "activity": [{"score": 10, "another_thing": 90}],
        "readiness": [{"score": 10, "ok": 567}],
    }
    monkeypatch.setattr(batch, "get_data_for_dates", lambda x, y: mock_response)
    results = client.get("/latest_scores")
    expected_response = {"activity": 10, "readiness": 10, "sleep": 10}
    assert json.loads(results.data) == expected_response
