import json
import logging

import requests

from requests_oauthlib import OAuth2Session

AUTH_URL = "https://cloud.ouraring.com/oauth/authorize"
TOKEN_URL = "https://api.ouraring.com/oauth/token"

with open(".credentials.json", "rb") as f:
    CREDENTIALS = json.load(f)

CLIENT_ID = CREDENTIALS["CLIENT_ID"]
CLIENT_SECRET = CREDENTIALS["CLIENT_SECRET"]
REDIRECT_URI = "http://0.0.0.0:3030/callback"


def get_access_token() -> str:
    """
    Access tokens require permissions from the user, oura server, and this application.
    Essentially, we need your permission to access health information from oura's servers.
    This process asks you to provide that permission by giving us the corresponding code.
    Once we have the access token, we can display useful info to you.

    Example:

    WARNING:root:Accept permissions in the URL:
    https://cloud.ouraring.com/oauth/authorize?response_type=code&client_id=SOME_ID&
    redirect_uri=http%3A%2F%2F0.0.0.0%3A3030%2Fcallback&state=SOME_STATE

    where SOME_ID = your client id
    and SOME_STATE = some string generated by the application server.

    You'll get redirected to a some broken page like
    http://0.0.0.0:3030/callback?code=SOME_CODE&state=SOME_STATE

    where SOME_CODE is what you want.

    Take the the code from the response URL and paste it here.
    SOME_CODE

    And voila! We have the access token.
    """
    session = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI)
    authorization_url, state = session.authorization_url(AUTH_URL)
    logging.warning("Accept permissions in the URL:\n{}".format(authorization_url))

    code = input("Take the the code from the response URL and paste it here.\n")

    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
    }
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    response = requests.post(TOKEN_URL, data=data, auth=auth).json()
    access_token = response["access_token"]
    return access_token