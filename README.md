## 1. UseCase
基本的にどなたでもご利用いただけますが、作成する際Starを押していただければ幸いです。
下記手順で進めると、<span style="color: blue; ">Django × Next.js</span> の環境が立ち上がります。

### 2. git clone後の初期設定(.env等の新規作成)
```shell
# configの作成
$ cp -R nextjs/config_sample nextjs/config

# docker-compose用の.envファイルの作成
$ cp .env.sample .env

#Django用の.envファイルの作成
$ cp django/.env.sample django/.env
```

### 3. Dockerコンテナの作成
```shell
# Docker Imageの作成
$ docker compose build

# DOcker Imageからコンテナの作成
$ docker compose up -d
```

### 4. Owner
* 永松光平
* kohei0801nagamatsu@gmail.com
* 2022/08/15 作成
