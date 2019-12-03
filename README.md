# simple-scoreboard-backend

简易的分数排行榜后端。使用 HTTP GET 请求完成数据上传与下载。

## 用法

### 保存玩家传来的分数（/save）

    HTTP GET: http://127.0.0.1:5000/save?name=jonb&score=20

### 玩家获取排行榜（/score）