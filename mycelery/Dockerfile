FROM python:3.13-slim

# avoid pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# set work directory
WORKDIR /mycelery

# install uv
RUN pip install uv

#copy requiremets
COPY pyproject.toml /mycelery/
COPY uv.lock /mycelery/

#sync dependencies

RUN uv sync --locked

#copy project
COPY . /mycelery

EXPOSE 8000
