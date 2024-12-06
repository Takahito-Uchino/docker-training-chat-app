# Docker研修用Chat App
- Docker研修で使用するChat Appです
- RareTECHのハッカソン初級用を流用しています
- ./docker/ にはDocker Compose用のDockerfileが格納されています
- ./docker_individual/にはDocker Composeを使わずに個別にコンテナを起動する場合のDockerfileが格納されています
- compose.yamlは演習問題ように未完成となっています
  - 答え
  - 13行目: docker/db/Dockerfile
  - 17行目: mysql_data:/var/lib/mysql
  - 47行目: docker/app/Dockerfile
  - 55行目: "8080:5000"
### 講義テキスト(アクセス制限あり)
  - https://docs.google.com/presentation/d/1InGZXHNsphwafLUjR8l1BoDQ0RKig8XhlPAt75bj4kE/edit#slide=id.p