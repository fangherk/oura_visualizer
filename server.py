from datetime import date, timedelta

from flask import Flask, jsonify

from batch import get_data_for_dates

app = Flask(__name__, template_folder="dist", static_folder="dist", static_url_path="")


@app.route("/")
def home():
    return app.send_static_file("index.html")


@app.route("/latest_scores", methods=["GET"])
def latest_scores():
    yesterday = date.today() - timedelta(days=1)
    data = get_data_for_dates(yesterday, yesterday)

    # Find a way to check if key exists before getting values.
    readiness = data["readiness"][0]["score"]
    sleep = data["sleep"][0]["score"]
    activity = data["activity"][0]["score"]
    scores = dict(readiness=readiness, sleep=sleep, activity=activity)

    response = jsonify(scores)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    app.run(debug=True)
