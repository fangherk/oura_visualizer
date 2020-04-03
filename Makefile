.PHONY: lint
lint: 
	fd . -t f -E '*\.{py,lock,toml}' -E 'Makefile' | xargs yarn prettier --write
