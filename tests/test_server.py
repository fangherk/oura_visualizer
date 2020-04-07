import json
from datetime import date, timedelta
from random import randint
from typing import Any, Dict

import pytest

from backend import batch
from backend.server import app, get_value_date


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


def test_all_data(client, monkeypatch):
    # TODO: use a temp mock instead of randomly generating values
    def helper(n : int) -> Dict[str, Any]:
        date_str = (date(2020, 1, 1) + timedelta(days=n)).strftime("%Y-%m-%d")
        return {"score": randint(0, 100), "summary_date": date_str}

    mock_response = {
        "sleep": [helper(n) for n in range(20)],
        "activity": [helper(n) for n in range(20)],
        "readiness": [helper(n) for n in range(20)],
    }
    monkeypatch.setattr(batch, "get_data_for_dates", lambda x, y: mock_response)
    results = client.get("/all_data")
    expected_response = {
        "sleep": [get_value_date(day) for day in mock_response["sleep"]],
        "activity": [get_value_date(day) for day in mock_response["activity"]],
        "readiness": [get_value_date(day) for day in mock_response["readiness"]],
    }
    assert json.loads(results.data) == expected_response


def test_get_value_date():
    day = {"score": 12, "summary_date": "2020-02-03", "other_stuff": 132}
    result = get_value_date(day)
    assert result == {"value": 12, "date": "2020-02-03"}
