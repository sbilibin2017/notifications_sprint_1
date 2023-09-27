FROM python:3.10

# set env variables
ENV HOME=/
ENV APP_HOME=/app
ENV GROUP=app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# create directory with app
WORKDIR ${APP_HOME}

# add code
COPY bin bin
COPY libs libs
COPY pyproject.toml pyproject.toml

# install packages
RUN apt-get update \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev

# add security
RUN groupadd -r $GROUP && \
    useradd -d $APP_HOME -r -g $GROUP $GROUP && \
    chown $GROUP:$GROUP -R $APP_HOME   
USER $GROUP

# run app
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "bin.__main__:app", "--bind", "0.0.0.0:8000"]
