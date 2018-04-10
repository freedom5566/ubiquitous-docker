# Julia

alpine 現在也有Julia 的 [pack](https://pkgs.alpinelinux.org/package/edge/community/x86_64/julia "pkgs")     
`0.6.2-r1`      
images SIZE： 142MB     
裏面明明說安裝大小是61.59 MB        
稍微查了一下，依賴不少......

不過用上alpine至少從500多MB減少到142MB也算瘦身很多了

不過強迫症發作希望能夠在100MB以下......

`apk del --purge -r`好像沒啥用O_O

之後試試從原始碼建構好了

先放個連結

[Julia GitHub](https://github.com/JuliaLang/julia "github庫")      
[Julia dependencies ](https://github.com/JuliaLang/julia#required-build-tools-and-external-libraries "依賴項目")