# docker-compose
node+mariadb+phpmyadmin

#### 為甚麼我要這樣做？自尋煩惱？ 

由於我的筆電是2007出產的輕筆電       
以下是規格       
CPU:Intel U7300 1.3GZH      
RAM:2GB
GPU:當然是沒有XDD        
就算裝linux開機RAM就會用掉400~500MB，平常寫程式都嘛要開瀏覽器查資料，邊開邊寫這時候大概就會用掉1G(這時候就會頓頓的)，再開個編輯器就衝上1.3G了(除非我只用vim......)，更別說如果我要寫網頁裝個`LAMP`或是`LNMP`之類的，我根本卡到爆炸阿      
而且為了寫程式在筆電裝一堆有的沒的，久了就是一堆難以清理的頑垢.....，我還記得我上次裝個`wine`，Ubuntu的Unity桌面莫名其妙就爆炸了:sob:我超崩潰

那時候docker剛盛行，我一看就覺得根本是我的救星阿......，超低成本安裝各種環境，想刪掉就刪掉，想升級就升級，爆了也沒差

現在要寫甚麼語言需要建立甚麼環境，第一件事情就是先上docker hub找！ 

#### 此篇目標

使nodejs可以連線到mariadb（不同container、不同image）        
做這件事碰到蠻多問題的......，我一度覺得我幹嘛不直接pull那些node+postgres或是node+mongodb就好，但是碰到困難不能直接放棄


#### 怎麼做

如何在docker下使用node連到mariadb?

1. pull一個node images        

要拿來當基礎images
```sh
~$ docker pull node:8.10.0-alpine
```

等等會用到

2. 建立目錄跟新增packge.json
```sh
~$ mkdir nodeMariadb && cd nodeMariadb && vim packge.json
```
*packge.json*
```json
{
  "name": "app",
  "version": "1.0.0",
  "main": "index.js",
  "license": "MIT",
  "dependencies": {
    "node-gyp": "^3.6.2",
    "mariasql": "^0.2.6"
  }
}

```
裝mariasql沒有先裝node-gyp會跳錯，而裝node-gyp又需要`python2.7`、`mark`、`gcc/g++`，所以我們的dockerfile這樣寫

3. `vim` Dockerfile

```dockerfile
FROM node:8.10.0-alpine 
#第一步pull的images
RUN mkdir -p /usr/src/app 
#創建一個資料夾，拿來放node安裝後的文件
WORKDIR /usr/src/app 
#切換目錄
COPY package.json /usr/src/app 
#複製package.json進去容器的/usr/src/app資料夾

RUN sed -i 's/http\:\/\/dl-cdn.alpinelinux.org/https\:\/\/ftp.yzu.edu.tw\/Linux/g' /etc/apk/repositories && \
    apk --no-cache --virtual build-dependencies add \
    python \
    make \
    g++ \
    && echo "#undef LIBC_HAS_BACKTRACE_FUNC" > /usr/include/execinfo.h \
    && yarn \
    && apk del build-dependencies 
# sed -i 's/http\:\/\/dl-cdn.alpinelinux.org/https\:\/\/ftp.yzu.edu.tw\/Linux/g' 是把fetch目標改成國內唯一載點元智大學，不然慢到哭
# 安裝上述提到的python2、mark、gcc/g++
# echo "#undef LIBC_HAS_BACKTRACE_FUNC" > /usr/include/execinfo.h，沒有這行會跳錯說你沒有這檔案.....
# 終於能yarn安裝node-gyp、mariasql了 



CMD [ "node" ]
```

4. 建置dockerfile

```sh
~ nodeMariadb $ docker build -t node/db .
```
如果沒有意外應該會成功，然後`docker images`應該可以看到node/db，大約150MB

5. 啟動node/db，並把app複製出來

```sh
~ $ docker run --rm -ti node/db /bin/sh
```
再開一個終端機
```sh
~ $ docker ps
```
找到node/db container ID

```sh
~ $ docker cp c7b3a42e1fc0:/usr/src/app/ /nodeMariadb/
```
試著`du -sh nodeMariadb`，居然有60M......

這個步驟可以嘗試看看能不能連上mariadb

6. 新增docker-compose.yml

```sh
~ nodeMariadb $ vim docker-compose.yml
```

```yml
version: "3"
services: 
  db: 
    image: mariadb:latest
    environment:
      MYSQL_ROOT_PASSWORD: 123
    volumes:
      - /home/louis/database:/var/lib/mysql
    networks:
      - my_network 
  phpmyadmin:
    depends_on:
      - db
    image: phpmyadmin/phpmyadmin:latest
    ports:
      - 8081:80
    networks:
      - my_network
  node:
    image: node:8.10.0-alpine
    depends_on:
      - db
    volumes:
      - /home/louis/nodeMariadb/app/app:/usr/src/myapp
    networks:
      - my_network
    tty: true      
networks:
    my_network:

```

這邊注意node images用的是最一開始乾淨的node不是node/db


新增一個`query.js`

```js
var Client = require('mariasql');

var c = new Client({
  host: 'db',
  user: 'root',
  password: '123',
  charset :'utf8'
});

c.query('SHOW DATABASES', function(err, rows) {
  if (err)
    throw err;
  console.dir(rows);
});

c.end();
```
7. 使用docker-compose

```sh
~ nodeMariadb $ docker-compose up
```

再開一個終端機

```sh
~ $ cd nodeMariadb && docker-compose ps
```
確認服務都啟動了，就連進node吧

```sh
~ nodeMariadb $ docker-compose exec node sh
```
切換目錄
```sh
/  cd /usr/src/myapp
```
執行`query.js`
```sh
node query.js
```

應該可以看到你所建立的所有database

更多用法可以參考[mariasql Github](https://github.com/mscdex/node-mariasql "mariadbsql github")

弄到這邊仔細想想，真的有人會用node去連mariadb嗎XD