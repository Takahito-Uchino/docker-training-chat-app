# MySQL8系のイメージを指定
FROM mysql:8.0

# 環境変数を設定
ENV MYSQL_ROOT_PASSWORD=root\
    MYSQL_DATABASE=chatapp\
    MYSQL_USER=testuser\
    MYSQL_PASSWORD=testuser

# MySQLのローカルの設定ファイルをコンテナにコピー
COPY docker/db/my.cnf /etc/mysql/conf.d/my.cnf
# init.sqlをコンテナの/docker-entrypoint-init.db.dと共有
COPY docker/db/init.sql /docker-entrypoint-initdb.d