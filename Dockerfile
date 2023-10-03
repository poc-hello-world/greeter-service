FROM python:3.12.0

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml ./
COPY poetry.toml ./
COPY poetry.lock ./

RUN poetry install --no-dev

COPY . .

EXPOSE 5002
ENTRYPOINT ["poetry", "run"]
CMD ["gunicorn", "-b0.0.0.0:5002", "app:app"]
