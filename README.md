# simple-scoreboard-backend

简易的分数排行榜后端。使用 HTTP GET 请求完成数据上传与下载。

## 用法

### 保存玩家传来的分数（/save）

    HTTP GET: http://127.0.0.1:5000/save?name=jonb&score=20

### 玩家获取排行榜（/score）

    HTTP GET: http://127.0.0.1:5000/score

返回样例

    jonb,30\njob,30\njonb,20

### 手动清空排行榜

    浏览器访问：http://127.0.0.1:5000/reset?token=PLEASE-CHANGE-ME

## 谁在使用

- [nlstudio/doodleJump](https://github.com/nlstudio/doodleJump) :  A C-written doodleJump-like minigame in command line.