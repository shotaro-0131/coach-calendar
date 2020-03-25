# Docker Hubにあるpythonイメージをベースにする
FROM python:3.6-alpine
# FROM nginx:latest
# 環境変数を設定する
ENV PYTHONUNBUFFERED 1

# コンテナ内にcodeディレクトリを作り、そこをワークディレクトリとする
RUN mkdir /code
WORKDIR /code


# ホストPCにあるrequirements.txtをコンテナ内のcodeディレクトリにコピーする
# コピーしたrequirements.txtを使ってパッケージをインストールする
ADD requirements.txt /code/
RUN apk --update-cache add python3-dev  \
    gcc g++ libc-dev linux-headers 
# RUN apk add mariadb-client
# RUN apk add libssl-dev
# RUN apk add libpcre3-dev

RUN apk add python3-dev
RUN apk add --update mariadb-dev
RUN apk add mysql-client mysql-dev
RUN pip install -r requirements.txt 
# RUN apk del g++ mariadb-dev
# RUN apk add --no-cache mariadb-client-libs
# RUN pip install -r requirements.txt

# ホストPCの各種ファイルをcodeディレクトリにコピーする
ADD . /code/
CMD ["pip", "list"]
CMD ["nginx", "-g", "daemon off;","-c","/etc/nginx/nginx.conf"]
# CMD ["uwsgi", "--http", ":8000",  "--wsgi-file", "sanka.wsgi"]
# CMD ["uwsgi","--ini","uwsgi.ini"]
CMD ["uwsgi","--http", ":8000", "--module", "sanka.wsgi"]