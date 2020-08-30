db-name = postgres
db-user = user

build-dev:
	-cp -n ./config/.env.template ./config/.env
	docker-compose build

up-dev:
	docker-compose run --rm backend python manage.py migrate
	docker-compose up
	make load-fixtures

migrations:
	docker-compose exec backend bash -c "./manage.py makemigrations && ./manage.py migrate"

load-fixtures:
	docker-compose exec backend bash -c "./manage.py migrate && \
    ./manage.py loaddata fixtures/dev_users.json"

test:
	docker-compose exec backend bash -c "pytest"

check:
	docker-compose exec backend bash -c "black server & flake8 server & mypy server"

recreate-db:
	docker-compose stop backend
	docker-compose exec db bash -c "dropdb $(db-name) -U $(db-user) && \
	createdb $(db-name) -U $(db-user)"
	docker-compose up -d backend
	make migrations

backend-bash:
	docker-compose exec backend bash

django-shell:
	docker-compose exec backend bash -c "./manage.py shell_plus"
