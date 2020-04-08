.DEFAULT_GOAL := help

### help - Help docs for this Makefile
.PHONY: help
help :
	@sed -n '/^###/p' Makefile

.PHONY: install
### install -- install packages using poetry and yarn
install:
	poetry install
	yarn install

.PHONY: lint
### lint -- lint the directories, requires fd to be installed
lint:
	fd . -t f -E '*\.{py,lock,toml}' -E 'Makefile' | xargs yarn prettier --write
	black .

.PHONY: dev
### frontend -- start the parcel server
frontend:
	yarn parcel static/index.html

.PHONY: backend
### backend -- start the backend server
backend:
	python -m backend.server

.PHONY: redis
### redis -- start redis server
redis:
	redis-server

.PHONY: test
### test -- test python code
test:
	pytest tests

.PHONY: clean
### clean - remove generated files
clean:
	rm -r dist/
