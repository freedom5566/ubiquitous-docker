FROM python:2.7-alpine3.7
COPY requirements.txt /code/
RUN apk add --no-cache mariadb-dev g++ && \
    pip install --no-cache-dir -r /code/requirements.txt && \
    apk del g++ mariadb-dev && \
    apk add --no-cache mariadb-client-libs
CMD ["python"]

