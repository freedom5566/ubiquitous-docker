# docker-compose
python+mariadb+phpmyadmin

1. 把python建置起來
```sh
~$ docker build --network=host -t python/db .
```
這邊有個問題，直接建置有時候會一直卡在
```
fetch http://dl-cdn.alpinelinux.org/alpine/v3.7/main/x86_64/APKINDEX.tar.gz
```
爬文很久，最直接的方式就是加`--network=host`......雖然還是很慢

2. docker-compose建立起來
一開始python一啟動就直接退出了，加個`tty:true`就可以了

3. 用python嘗試連接mariadb吧 

```sh
~$ docker-compose exec py sh
```
這邊注意一件事`exec`連的是service name，不是容器名字
```sh
/ python
```
```sh
>>> import MySQLdb
>>> MySQLdb.connect(host="db", user="root", passwd="123", db="HelloTest")
<_mysql.connection open to 'mysql' at 55f032a2bbb8>
```
