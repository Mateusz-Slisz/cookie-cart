# Cookie Cart
Simple app for adding items to cookie cart

# Development
#### To start development server you have to:
Build images
> It will generate also a .env file, based on .env.template. 
If you already have one, you should delete its to prevent conflicts or/and missing env variables.

```
make build-dev
```

Start images
```
make up-dev
```

# Testing & formatting
To run tests use
```
make test
```
To check code through black, flake8, isort and mypy, run 
```
make check
```

## Admin panel
If you want to use admin panel, load development users using fixtures
```
make load-fixtures
```
and use these credentials:
```
u: admin
p: smokesletsgo
```

## API Docs
API Documentation is available at [localhost:8000/swagger](http://localhost:8000/swagger).

## Other useful commands:
Run make-migrations and migrate
```
make migrations
```
Run shell in django env
```
make django-shell
```
Recreate DB
```
make recreate-db
```
