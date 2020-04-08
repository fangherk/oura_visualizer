# Oura Visualizer

## Context + Motivation

Curious to see what it would be like to build a simple dashboard displaying some health stats.

## How to use

Add a `.credentials.json` with `CLIENT_ID` and `CLIENT_SECRET` found on the Oura app.
Run redis with the defaults locally (planning to add docker, so this doesn't need to be done).

To install packages, run `make install`.
To start redis, run `make redis`.
To start the frontend, run `make frontend`.
To start the flask server, run `make backend`.
To start the batch pipeline, run: `make batch`.

The current result can either be found on http://localhost:5000/ or http://localhost:1234/ !


## Dependencies
1. Python 3+, with poetry installed -- for server auth + data
2. Yarn -- for the display
3. Docker -- for Redis

## Plan

0. Set up Oauth2 and cache access token.
1. Use dagster to run batch jobs to load syncs into the db.
2. Run HTTP requests off the db?, mainly polling for information.
3. Display information as a dashboard.

## What I Learned

1. Oauth 2 requires a lot of back and forth among user, app, and auth server.
2. Makefiles only like tabs
3. Patching the function directly doesn't seem to work, so path where it is pointed to. https://docs.python.org/3/library/unittest.mock.html#where-to-patch
