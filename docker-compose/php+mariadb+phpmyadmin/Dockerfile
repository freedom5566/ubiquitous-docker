FROM php:7.2-alpine3.7

RUN sed -i 's/http\:\/\/dl-cdn.alpinelinux.org/https\:\/\/ftp.yzu.edu.tw\/Linux/g' /etc/apk/repositories


RUN docker-php-ext-install pdo_mysql pdo
