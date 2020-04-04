.PHONY: lint
lint:
	fd . -t f -E '*\.{py,lock,toml}' -E 'Makefile' | xargs yarn prettier --write
	black .

.PHONY: dev
frontend:
	@ echo "Start parcel"
	yarn parcel static/index.html &

.PHONY: backend
backend:
	@echo "Start python"
	python server.py &

.PHONY: redis
redis:
	@echo "Start redis"
	redis-server &


.PHONY: all
all: frontend backend redis
	@echo "Everything is up!"
