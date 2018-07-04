# flask_docker_sample

FlaskをDocker で動かすサンプル。 Pipenvを使用

# PREREQUISITE
- Docker

# SETUP
```
$ git clone https://github.com/macinjoke/flask_docker_sample.git
$ cd flask_docker_sample
$ docker build -t flask_docker_sample .
```

# RUN
`$ docker run -it -p 5000:5000 -v $PWD:/app -e FLASK_ENV=development flask_docker_sample` など
