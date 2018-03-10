# 這篇是docker-compose一個範例

## 第一步

1. 新建立一個資料夾並切換過去

```bash
$ mkdir composetest
$ cd composetest
```

2. 建一個`app.py`新增以下程式碼後`:wq`退出
```bash
~/composetest$ vim app.py
```
```python
import time

import redis
from flask import Flask


app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
```

3. 新增一個`requirements.txt`增加以下模組後`:wq`退出

```
flask
redis
```
這邊的`requirements.txt`是為了讓docker的python可以使用
[flask](https://zh.wikipedia.org/wiki/Flask "wiki") 跟[redis](https://zh.wikipedia.org/wiki/Redis "wiki")

## 第二步：建立dockerfile

```bash
~/composetest$ vim Dockerfile
```
新增以下
```docker
FROM python:3.4-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```
這邊強行解說一下        
FROM:就是拉取一個用[alpine](https://zh.wikipedia.org/wiki/Alpine_Linux "wiki")包裝的[python3.4](https://github.com/docker-library/python/blob/55186d2c2c8b78bd8293293af42a5db3f815f332/3.4/alpine3.4/Dockerfile "dockerfileurl")images     
ADD:複製了一個本目錄`composetest`到 container的`/code`目錄       
WORKDIR:切換到`code`目錄       
RUN:pip安裝python要用的模組，這時候之前寫的`txt`檔案就是用在這裡的        
CMD:用python執行前面寫的`app.py`

## 第三步:主角登場，建立`compose.yml`檔案

```bash
~/composetest$ vim docker-compose.yml
```
```yml
version: '3'
services:
  web:
    build: .
    ports:
     - "5000:5000"
  redis:
    image: "redis:alpine"
```
再次強行解說      

version:Compose檔案格式版本，沒意外現在幾乎都是3       
services:可以塞入多個images       
web:下面的build:`.`建置dockerfile(python+flask)，然後映射5000port     
redis:拉取redis:alpine images

## 第4步用compose建立服務

```bash
~/composetest$ docker-compose up
```
然後開瀏覽器打開http://127.0.0.1:5000       
這一步有個問題 pip安裝的時候一直沒回應，重新啟動docker就可以了
網頁上應該會顯示
```text
Hello World! I have been seen 1 times.
```
按F5就會增加times.

關閉可以用直接在終端`CTRL+C`      
然後使用`down`清除容器。`--volumes`清除redis使用的資料
```bash
docker-compose down --volumes
```

# 參考連結

***

* [docker從入門到實踐簡中版](https://yeasy.gitbooks.io/docker_practice/content/ "gitbooklink")     
這本有有人fork用了[繁中版](https://www.gitbook.com/book/philipzheng/docker_practice/details "gitbooklink")可是年久失修囧，之後找機會幫忙pr看看

* [compose版本資料](https://docs.docker.com/compose/compose-file/ "dockerdocs")

* [compos此篇範例資料](https://docs.docker.com/compose/gettingstarted/#step-4-build-and-run-your-app-with-compose "dockerdocs")


