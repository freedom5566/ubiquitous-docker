# 紀錄docker建置各式環境碰到的問題


# 紀錄docker本身踩過的雷
現在不建議用--link了，突然有種學過的東西被時代淘汰的滄桑感?想到高中的vb6.0......

如何使用netwrok把mariadb+phpmyadmin連起來?

1. 建立docker network

```sh
~$ docker network create my_network
```
2. 啟動mariadb並加進網路
```sh
~$ docker run --name mariadb -v $PWD/database:/var/lib/mysql --network my_network  -e MYSQL_ROOT_PASSWORD=123 -d mariadb
```
3. 找到mariadb容器的IP

```bash
~$ docker inspect mariadb |grep IPAdd
```
應該會列出
```bash
            "SecondaryIPAddresses": null,
            "IPAddress": "",
                    "IPAddress": "172.18.0.2",
```
4. 啟動phpmyadmin
```bash
~$ sudo docker run  -d --network my_network -e PMA_HOST=172.18.0.2 -p 8081:80 phpmyadmin/phpmyadmin
```
PMA_HOST如果不填，phpmyadmin就連不進mariadb哦!

## 解決fetch Alpine 的時候總是卡住的問題

辦法1
```dockerfile
RUN sed -i 's/http\:\/\/dl-cdn.alpinelinux.org/https\:\/\/ftp.yzu.edu.tw\/Linux/g' /etc/apk/repositories
```
元智大學太猛啦！！！！666666666666         
趕超四大四中餒
台灣唯一載點......

辦法2
```sh
~$ docker build --network=host -t yourimaegesname .
```
兩個實際嘗試後，辦法1比較快，快超多！

[alpine各地載點目錄](https://git.alpinelinux.org/cgit/aports/tree/main/alpine-mirrors/mirrors.yaml "good!")
## 環境
***
> docker版本:docker-ce 17.05
