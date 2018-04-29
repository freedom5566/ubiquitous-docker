FROM alpine:3.7

RUN sed -i 's/http\:\/\/dl-cdn.alpinelinux.org/https\:\/\/ftp.yzu.edu.tw\/Linux/g' /etc/apk/repositories  \
    && apk add --no-cache --update \ #我不確定是不是大葉的問題，我不用update會出現指令miss的情況
    tg \
    &&  rm -rf /var/cache/apk/* /tmp

CMD ["/usr/bin/telegram-cli"]
