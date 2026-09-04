.PHONY: build up down logs test

build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

test:
	python3 tests/test_integration.py -v
