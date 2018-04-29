FROM alpine:3.7

RUN sed -i 's/http\:\/\/dl-cdn.alpinelinux.org/https\:\/\/ftp.yzu.edu.tw\/Linux/g' /etc/apk/repositories && \
    apk add --no-cache \
    tg
    
CMD ["/usr/bin/telegram-cli"]
