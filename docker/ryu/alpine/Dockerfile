FROM python:2.7-alpine3.7

WORKDIR /root

RUN sed -i 's/http\:\/\/dl-cdn.alpinelinux.org/https\:\/\/ftp.yzu.edu.tw\/Linux/g' /etc/apk/repositories \
    && apk add --no-cache  --update \
    curl \
    py-setuptools \
    py-eventlet \
    py-lxml \
    py-msgpack \
    iproute2 \
    && curl -kL https://github.com/osrg/ryu/archive/master.tar.gz | tar -xvz \
    && cd ryu \
    #&& pip install --default-timeout=100  . \
    && pip install --default-timeout=100 -r tools/pip-requires \
    && python setup.py install \
    

CMD ["ryu-manager"]
