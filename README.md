# 根据自己习惯写的一款成功率高达33%的世界上最简单的扫描器，漏洞要么存在要么不存在要么被拉黑

# RWD-Scan
## 安服仔必备，不想努力就用它

可以把项目上常见的场景添加到dict.txt，然后在做授权的安全服务项目的时候就可以一把梭

index.py暂时无用，留着以后做集成，可以单独运行DirScan、DirScans、UrlScan，会根据目标状态码生成对应的结果文件。为了简化输出，有些状态码不会显示在控制台，比如400，请注意查看对应结果文件

### UrlScan -批量扫存活，输出网站标题
```bash
python UrlScan.py -u url.txt
```

### DirScan  -扫目录，输出网站标题、响应长度、目标使用的server
```bash
python DirScan.py -u https://url -f dict.txt
```

### DirScans  -批量扫目录，输出网站标题、响应长度、目标使用的server
如果没有参数，默认扫描当前目录下的url.txt，请确保目录下有目标url.txt以及字典文件dict.txt，如果要指定文件，请使用-h查看帮助
```bash
python DirScans.py
```

目录扫描最好是`不要以斜杠结尾`

url扫描最好是`加上http或https`
(这两条可以自己加个if优化)

根据结果收集有用的信息（图为自己搭建的靶场）
<img width="1080" alt="1" src="https://user-images.githubusercontent.com/45167857/170027329-90b9b293-ee77-4936-b6be-e349a8faa8f2.png">
<img width="720" alt="dirscan" src="https://user-images.githubusercontent.com/45167857/170027905-c4d938d5-2ece-4a0c-9edd-5f6766b630b8.png">


# 法律
```bash
本工具仅能在取得足够合法授权的企业安全建设中使用在使用,
本工具过程中，您应确保自己所有行为符合当地的法律法规。
如您在使用本工具的过程中存在任何非法行为，您将自行承担所有后果，本工具所有开发者和所有贡献者不承担任何法律及连带责任。
除非您已充分阅读、完全理解并接受本协议所有条款，否则，请您不要安装并使用本工具。
您的使用行为或者您以其他任何明示或者默示方式表示接受本协议的，即视为您已阅读并同意本协议的约束
```
