# 快速重建php專案

# 這一切都非常不優雅，請勿模仿

本來想用ADD 可是不支援zip解壓縮
使用 apk add --no-cache --virtual....
作git clone時會產生警告，不過沒有大礙

不想看到警告可以

apk --update add --no-cache --virtual
//結尾不加rm -rf /var/cache/apk/*       
然而這並不優雅
[docker-alpine包用法](https://github.com/gliderlabs/docker-alpine/blob/master/docs/usage.md "github")

這樣做只是多fetch一次，雖然這樣警告就會消失了，但images大小也會增加
