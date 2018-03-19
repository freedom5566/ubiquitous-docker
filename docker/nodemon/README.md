# 把nodemon打包成一個images

然後運行容器
```sh
$ docker run --rm -ti -v $PWD:/usr/src/myapp -p 8080:3000 -d nodemon
```

就可以快樂的寫node啦~~
