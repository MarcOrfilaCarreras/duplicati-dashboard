FROM ubuntu:20.04

RUN apt-get update && apt-get install --no-install-recommends -y \
    python3-dev \
    python3-pip \
&& rm -rf /var/lib/apt/lists/*

RUN mkdir /app
COPY app /app
WORKDIR /app

RUN pip3 install -r requirements.txt

RUN groupadd -r gunicorn && useradd --no-log-init -r -g gunicorn gunicorn

RUN chown -R gunicorn:gunicorn /app

USER gunicorn

EXPOSE 7575

ENTRYPOINT [ "gunicorn" ]
CMD ["--bind", "0.0.0.0:7575", "entrypoint:app"]
