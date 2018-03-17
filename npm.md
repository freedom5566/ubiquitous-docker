### npm在docker下基本上都會卡住的問題

本來是想裝個Eslint

可是eslint --init 只能用npm，不能用yarn
[eslint討論過不加yarn方法](https://github.com/eslint/eslint/pull/9023 "github")
在docker基本上動不了

想說去`bin/eslint.js -->lib/config/config-initializer.js -->util/npm-util-->function installSyncSaveDev`
改改看好了，但是看起來好厚工=_=

這時候又看到有人說可以[eslint --init --registry=otherregistry](https://github.com/naseeihity/LearnToLearn/issues/31)
但是了一下台灣好像沒有自己的mirror，
直接用yarn的https://registry.yarnpkg.com試試
居然成功建立了......震驚

不過剛剛突然想到我幹嘛不直接`--network=host`.....
