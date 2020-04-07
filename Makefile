.DEFAULT_GOAL := all

.PHONY: install
### install -- install packages using poetry and yarn
install:
	poetry install
	yarn install

.PHONY: lint
### lint -- lint the directories 
lint:
	fd . -t f -E '*\.{py,lock,toml}' -E 'Makefile' | xargs yarn prettier --write
	black .

.PHONY: dev
### frontend -- start the parcel server
frontend:
	yarn parcel static/index.html &

.PHONY: backend
### backend -- start the backend server
backend:
	python server.py &

.PHONY: redis
### redis -- start redis server
redis:
	redis-server &
	
.PHONY: all
### all - start everything
all: frontend backend redis

.PHONY: clean
### clean - remove generated files
clean:
	rm -r dist/

.PHONY: help
help : Makefile
	@sed -n 's/^###/p' $<

