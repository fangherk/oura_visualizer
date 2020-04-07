from datetime import date

import requests

import redis
from dagster import pipeline, solid

from . import oura_auth

r = redis.Redis(host="localhost", port=6379, db=0)

if not r.get("access_token"):
    access_token = oura_auth.get_access_token()
    r.set("access_token", access_token, ex=86400)

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


def get_data_for_dates(start, end):
    """
    Get sleep, activity, and readiness data for a start - end dates.
    Data should be returned as a map of
    {
      'sleep' : List[Dict[Any]],
      'activity' : List[Dict[Any]],
      'readiness' : List[Dict[Any]],
    }
    """
    sleep_url = get_endpoint_url(SLEEP_PARAMS, start, end)
    activity_url = get_endpoint_url(ACTIVITY_PARAMS, start, end)
    readiness_url = get_endpoint_url(READINESS_PARAMS, start, end)
    data = {}
    for url in [sleep_url, activity_url, readiness_url]:
        response = requests.get(url).json()
        data.update(response)
    return data


@solid
def get_data(context):
    """ Extract data. """
    start = date(2000, 1, 1)
    end = date(2020, 4, 1)

    data = get_data_for_dates(start, end)
    for key, values in data.items():
        context.log.info("Found {num} {key} summaries".format(num=len(values), key=key))
    return data


@pipeline
def get_all_data():
    get_data()
