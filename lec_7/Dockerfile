FROM ubuntu

RUN ["adduser", "ai"]
RUN ["whoami"]

# 기존사용자(root) -> 현재 사용자를 ai로 변경
USER ai
RUN ["whoami"]