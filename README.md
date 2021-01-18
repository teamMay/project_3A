# MAY - Project ECM 3A 2021

This is a project for student from [Ecole Centrale Marseille](https://www.centrale-marseille.fr) aiming to discover sentiment analysis through different methods and serve an AI model through a website or an API.

## Sentiment analysis served through a web API

For local development, we use [FastAPI](https://fastapi.tiangolo.com/) directly.

For production means, we can use FastAPI in pair with [Traefik](traefik.io).

## Local install

You need `python` (3.6+), `pip` and `python3-venv` installed.

If python isn't installed on your machine, follow official documentation.

If you're only missing pip:

```bash
# unix
sudo apt install python3-pip
```

python3-venv:

```bash
# unix
sudo apt install python3-venv
```

First, let's install `pipx` and `poetry`.

```bash
# pipx
pip3 install pipx
python3 -m pipx ensurepath
python3 -m pipx completions

# poetry
pipx install poetry
# You may need to restart your terminal for poetry to be taken into account
```

Finally, we can install our dependencies:

```bash
poetry install
```

## Run

To launch uvicorn (application server), use:

```bash
cd app
uvicorn main:app --reload
```

With poetry managing your installation:

```bash
poetry run uvicorn app.main:app --port 8080 --reload
```

You can now browse to your [fastapi website](http://localhost:8080/docs).

This should lead you to an error page since we haven't defined anything on the root of our application.

However, FastAPI comes with auto documentation. Browse to the [documentation](http://localhost:8080/docs) and you can see you first route ready to go !

So far, only one API route has been defined:

http://localhost:8080/sentiment-analysis

## Testing

```bash
cd app
poetry run pytest
```