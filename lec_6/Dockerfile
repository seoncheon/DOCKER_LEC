FROM ubuntu

# 30초 간격으로 특정 사이트 접속 체크, 응답 지연은 30초 이내에 들어올 때까지는 오류 없음
HEALTHCHECK --interval=30s --timeout=30s CMD [ "curl", "-f", "http://127.0.01", "||", "exit 1" ]

# DB 체크 예시
# HEALTHCHECK --interval=30s --timeout=30s CMD [ "mysqladmin", "ping", "-h", "127.0.01", "--password=12341234", "--silent" ]