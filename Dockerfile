# Docker Hubにあるpythonイメージをベースにする
FROM python:3.6-alpine

# 環境変数を設定する
ENV PYTHONUNBUFFERED 1

# コンテナ内にcodeディレクトリを作り、そこをワークディレクトリとする
RUN mkdir /code
WORKDIR /code


# ホストPCにあるrequirements.txtをコンテナ内のcodeディレクトリにコピーする
# コピーしたrequirements.txtを使ってパッケージをインストールする
ADD requirements.txt /code/
RUN apk --update-cache add python3-dev postgresql-client \
    gcc g++ libc-dev linux-headers postgresql-dev
# RUN apk add mariadb-client
RUN apk add python3-dev
RUN apk add --update mariadb-dev
RUN apk add mysql-client mysql-dev
RUN pip install -r requirements.txt 
# RUN apk del g++ mariadb-dev
# RUN apk add --no-cache mariadb-client-libs
# RUN pip install -r requirements.txt

# ホストPCの各種ファイルをcodeディレクトリにコピーする
ADD . /code/
