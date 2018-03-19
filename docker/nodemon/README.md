# 把nodemon打包成一個images

專案資料夾要先裝好nodemon哦！！！       
然後運行容器
```sh
$ docker run --rm -ti -v $PWD:/usr/src/myapp -p 8080:3000 -d nodemon
```
如果你想看到log就不要加`-d`     
或是

`$ docker container logs [container ID or NAMES]`
就可以快樂的寫node啦~~
