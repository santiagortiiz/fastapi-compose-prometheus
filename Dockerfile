# The builder image, used to build the virtual environment
FROM python:3.11-bullseye as builder

# Install package manager
RUN pip install poetry==1.7.1

# Define environment
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

# Set work directory
WORKDIR /fastapi

# Copy project dependencies
COPY pyproject.toml poetry.lock ./

# Install production dependencies only and remove poetry cache directory
RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

# The runtime image, used to run the service
FROM python:3.11-slim-bullseye as runtime

# Set virtual environment path and add it to the system Path
ENV VIRTUAL_ENV=/fastapi/.venv \
    PATH="/fastapi/.venv/bin:$PATH"

# Copy project dependencies from builder stage
COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

# Copy project code
COPY app/ /fastapi/app/

# Set work directory
WORKDIR /fastapi

# Run service
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
