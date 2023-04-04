# 베이스 이미지
FROM ubuntu

# 패키지 업데이트, nginx 설치
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install nginx

# 포트 expose
EXPOSE 80

# 빌드 완료 후 이미지를 기반으로 새로운 이미지를 빌드하면 실행할 명령   
ONBUILD ADD web.tar /var/www/html

# 컨테이너에서 실행할 명령
CMD ["nginx", "-g", "daemon off;"]