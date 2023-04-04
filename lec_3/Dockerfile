# 베이스 이미지
FROM ubuntu

# ubuntu os에서 nginx를 설치하기 위한 작업 -> 설치 관리자 레포지토리 최신으로 갱신
RUN apt-get -y update && apt-get -y upgrade
# nginx 설치
RUN apt-get -y install nginx

# EXPOSE, 이 이미지를 기반으로 만들어질 컨테이너의 공개 포트번호 지정
# nginx 웹서버이므로 통상 80 포트를 사용
EXPOSE 80

# nginx를 기본으로 설치하면, 환경 설정상 루트 디렉토리 (웹이 인식하는 물리적 경로)
# -> html을 기본적으로 어디다가 두는가 -> /var/www/html/*.html
ADD web.tar /var/www/html/

# COPY 연습
COPY readme.txt /var/www/html/readme2.txt

# 컨테이너가 만들어지고 실행되면 nginx가 가동 -> exec 방식으로 작성
CMD ["nginx", "-g", "daemon off;"]