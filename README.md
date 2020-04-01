# Oura Visualizer

## Context + Motivation
Curious to see what it would be like to build a simple dashboard displaying some health stats.

## Plan
1. Use dagster to run batch jobs to load syncs into the db.
2. Run HTTP requests off the db, mainly polling for information.
  - Introduce a cache?
3. Display information as a dashboard.
