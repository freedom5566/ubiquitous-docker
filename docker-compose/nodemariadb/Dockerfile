FROM node:8.10.0-alpine
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY package.json /usr/src/app

RUN sed -i 's/http\:\/\/dl-cdn.alpinelinux.org/https\:\/\/ftp.yzu.edu.tw\/Linux/g' /etc/apk/repositories && \
    apk --no-cache --virtual build-dependencies add \
    python \
    make \
    g++ \
    && echo "#undef LIBC_HAS_BACKTRACE_FUNC" > /usr/include/execinfo.h \
    && yarn \
    && apk del build-dependencies 

CMD [ "node" ]

