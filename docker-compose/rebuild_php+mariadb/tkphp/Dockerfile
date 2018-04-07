FROM php:7.2-alpine3.7

RUN sed -i 's/http\:\/\/dl-cdn.alpinelinux.org/https\:\/\/ftp.yzu.edu.tw\/Linux/g' /etc/apk/repositories  && \
    apk add --update --no-cache   --virtual build-dependencies  \
    git \
    && git clone https://github.com/freedom5566/bulletin-tkphp.git /usr/src/myapp/tp5 \
    && git clone https://github.com/top-think/framework /usr/src/myapp/tp5/thinkphp \
    && apk del build-dependencies \
    && docker-php-ext-install pdo_mysql 


