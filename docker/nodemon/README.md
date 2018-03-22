# 把nodemon打包成一個images

專案資料夾要先裝好nodemon哦！！！       
然後運行容器
```sh
$ docker run --rm -ti -v $PWD:/usr/src/myapp -p 8080:3000 -d nodemon run devserver
```
如果你想看到log就不要加`-d`     
     
或是使用以下命令查看

`$ docker container logs [container ID or NAMES]`       

現在我建議把nodemon ./bin/www寫在package.json的script來啟動
像這樣
```json
"scripts": {
    "start": "node ./bin/www",
    "devserver": "./node_modules/nodemon/bin/nodemon.js ./bin/www"
  },
```
一來這樣比較有彈性，二來這樣如果出錯yarn會幫你產生error.log   
現在可以快樂的寫node啦~~
