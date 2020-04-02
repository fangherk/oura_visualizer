from datetime import date

import requests

import redis
from dagster import pipeline, solid
from oura_auth import get_access_token

r = redis.Redis(host="localhost", port=6379, db=0)

if not r.get("access_token"):
    access_token = get_access_token()
    r.set("access_token", access_token)

TOKEN = r.get("access_token").decode("utf-8")

URL_BASE = "https://api.ouraring.com/v1/"
SLEEP_PARAMS = "sleep?start={}&end={}"
ACTIVITY_PARAMS = "activity?start={}&end={}"
READINESS_PARAMS = "readiness?start={}&end={}"
ACCESS = "&access_token={TOKEN}".format(TOKEN=TOKEN)


def get_endpoint_url(params: str, start: date, end: date) -> str:
    """ Return the endpoint url given endpoint, start, and end date. """
    form = "%Y-%m-%d"
    url = URL_BASE + params.format(start.strftime(form), end.strftime(form)) + ACCESS
    return url


start = date(2000, 1, 1)
end = date(2020, 4, 1)


@solid
def get_data(context):
    """ Extract data. """
    sleep_url = get_endpoint_url(SLEEP_PARAMS, start, end)
    activity_url = get_endpoint_url(ACTIVITY_PARAMS, start, end)
    readiness_url = get_endpoint_url(READINESS_PARAMS, start, end)
    data = {}
    for url in [sleep_url, activity_url, readiness_url]:
        data.update(requests.get(url).json())
    for key, values in data.items():
        context.log.info("Found {num} {key} summaries".format(num=len(values), key=key))
    return data


@pipeline
def get_all_data():
    get_data()
