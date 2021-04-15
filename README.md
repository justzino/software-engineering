<h1 align="center">Software Engineering</h1>

> This is a repository for 'Software Engineering' Class of Hongik Univ.

## Apache-docker 실습

### Dockerfile

```docker
FROM ubuntu
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y apache2
ADD . /var/www/html
ENTRYPOINT apachectl -D FOREGROUND
ENV test TestingENV
```

### Command

```shell
docker pull ubuntu
sudo docker run -it -d [ubuntu]
sudo docker exec -it [container ID] bash
sudo docker build . -t [생성할 image이름]
sudo docker run -it -p 5000:80 -v /home/ubuntu/[디렉토리 이름]:/var/www/html -d [image이름]
sudo docker run -it -p 5000:80 -v /home/ubuntu/docker:/var/www/html -d [image이름]
```

- /var/www/html/ 에 volume을 마운틴하는 이유 : apache의 index.html 파일이 해당 경로에 위치해 있기 때문
- /var/www/html/tmp.html 생성후 `서버주소/tmp.html` 접속 -> 제대로 mount 적용 되는지 확인

---

## Assignment1

### static website using github and template

> hosting url : https://justzino.github.io/hongik-software-engineering/

---

## Assignment2

### wordpress, php를 사용하여 웹 서비스 만들어 보기

- wordpress를 사용한 브라우저를 EC2 서버에 올리기

- 클라이언트에서 form 또는 button 같은 document object를 click 하여 서버로 데이터를 보내고 전송 받은 데이터에 따라 적절히 서비스를 다시 클라이언트에게 제공하는 dynamic 서비스를 wordpress를 이용하여 container로 만들어 봅니다.

- 만일 브라우저에서 데이터를 웹 서버에 보내어 그에 따라 서버가 여러분이 정해 놓은 작업을 수행하는 dynamic 서비스를 구현하는 방법을 모르거나 해 본 적이 없는 사람은 지난 번 static 웹 사이트 과제처럼 자기 이름 학번을 보여주는 wordpress 를 이용한 웹 서버를 container 로 만들어도 됩니다.

- dynamic 서비스를 만들 줄 아는 사람도 그냥 간단히 브라우저에서 이름을 입력하면 "안뇽, <입력한 이름>"이 브라우저에서 rendering 하는 매우 간단한 프로그램으로 충분하니 복잡한 서비스를 구현하여 너무 자랑하지 말기.

### Reference

- https://docs.docker.com/compose/wordpress/
