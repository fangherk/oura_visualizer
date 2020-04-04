# Oura Visualizer

## Context + Motivation

Curious to see what it would be like to build a simple dashboard displaying some health stats.

## How to use

Add a `.credentials.json` with `CLIENT_ID` and `CLIENT_SECRET` found on the Oura app.
Run redis with the defaults locally (planning to add docker, so this doesn't need to be done).
`dagster pipeline execute -f batch.py -n get_all_data`

The frontend uses react and parcel, which packages everything out of the box.
For running the frontend, use `make frontend`.

For running the flask server, just use `python server.py`.

## Plan

0. Set up Oauth2 and cache access token.
1. Use dagster to run batch jobs to load syncs into the db.
2. Run HTTP requests off the db?, mainly polling for information.
3. Display information as a dashboard.

## What I Learned

1. Oauth 2 requires a lot of back and forth among user, app, and auth server.
