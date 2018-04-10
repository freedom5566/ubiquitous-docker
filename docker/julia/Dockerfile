FROM alpine:3.7




RUN sed -i 's/http\:\/\/dl-cdn.alpinelinux.org/https\:\/\/ftp.yzu.edu.tw\/Linux/g' /etc/apk/repositories  \
    && apk update \
    && apk add --no-cache  \
    julia \
    && apk del --purge -r

CMD ["julia"]