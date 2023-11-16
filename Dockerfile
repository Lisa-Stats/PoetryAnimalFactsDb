FROM python:3.9.18

# Install poetry:
RUN pip install poetry

WORKDIR /app

# Copy only requirements to cache them in docker layer
COPY poetry.lock pyproject.toml /app/

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY . /app

ENTRYPOINT [ "python" ]
CMD ["poetryanimalfactsdb.py"]
