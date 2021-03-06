# MAY - Project ECM 3A 2021

This is a project for students from [Ecole Centrale Marseille](https://www.centrale-marseille.fr) aiming to discover sentiment analysis through different methods and serve an AI model via an API.

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

However, FastAPI comes with auto documentation. Browse to the [documentation page](http://localhost:8080/docs) and you can enjoy you first route ready to go !

So far, only one API route has been defined: http://localhost:8080/sentiment-analysis

## Testing

```bash
cd app
poetry run pytest
```

## Going further

I chose FastAPI because it's... fast !
You get documentation out of the box, validation etc etc with minimum configuration.

From here, you can:

* Use your own models and algorithms within existing routes or create new ones
* Deploy this website to a production server
* Try others alternatives like https://www.deploymachinelearning.com/ (django, docker, AB testing)
* Decide to create a frontend website (with React, Vue, Svelte or whatever framework) to consume your API

Feel free to reach me out at: adrien@may-sante.com
