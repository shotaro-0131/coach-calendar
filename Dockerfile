# Docker Hubにあるpythonイメージをベースにする
FROM python:3.6-alpine
# FROM nginx:latest
# 環境変数を設定する
ENV PYTHONUNBUFFERED 1

ARG DOCKER_FILE_ENV

# コンテナ内にcodeディレクトリを作り、そこをワークディレクトリとする
RUN mkdir /code
WORKDIR /code


# ホストPCにあるrequirements.txtをコンテナ内のcodeディレクトリにコピーする
# コピーしたrequirements.txtを使ってパッケージをインストールする
ADD requirements.txt /code/
RUN apk --update-cache add python3-dev  \
    gcc g++ libc-dev linux-headers 

RUN apk add python3-dev
RUN apk add --update mariadb-dev
RUN apk add mysql-client mysql-dev
RUN apk add postgresql-dev
RUN pip install -r requirements.txt 

# ホストPCの各種ファイルをcodeディレクトリにコピーする
ADD . /code/
CMD ["pip", "install", "--upgrade", "pip"]
#CMD ["gunicorn", "sanka.wgsi", "--log-file"]


#aws and local

#heroku
CMD python manage.py makemigrations
CMD ["python", "manage.py", "migrate"]
CMD gunicorn --bind 0.0.0.0:$PORT sanka.wsgi
