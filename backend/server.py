from datetime import date, timedelta
from typing import Any, Dict

from flask import Flask, jsonify

from . import batch

app = Flask(__name__, template_folder="../dist", static_folder="../dist", static_url_path="")


@app.route("/")
def home():
    return app.send_static_file("index.html")


@app.route("/latest_scores", methods=["GET"])
def latest_scores():
    yesterday = date.today() - timedelta(days=1)
    data = batch.get_data_for_dates(yesterday, yesterday)

    # Find a way to check if key exists before getting values.
    readiness = data["readiness"][0]["score"]
    sleep = data["sleep"][0]["score"]
    activity = data["activity"][0]["score"]
    scores = dict(readiness=readiness, sleep=sleep, activity=activity)

    response = jsonify(scores)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


def get_value_date(day: Dict[str, Any]) -> Dict[str, str]:
    return {"value": day["score"], "date": day["summary_date"]}


@app.route("/all_data", methods=["GET"])
def all_data():
    way_back_date = date(2019, 5, 5)
    data = batch.get_data_for_dates(way_back_date, date.today())

    # Find a way to check if key exists before getting values.
    readiness = [get_value_date(day) for day in data["readiness"]]
    sleep = [get_value_date(day) for day in data["sleep"]]
    activity = [get_value_date(day) for day in data["activity"]]
    scores = dict(readiness=readiness, sleep=sleep, activity=activity)

    response = jsonify(scores)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    app.run(debug=True)
