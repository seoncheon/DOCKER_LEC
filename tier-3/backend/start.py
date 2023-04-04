from flask import Flask 
import pymysql as my

# db host -> `db`:컴포즈에 기술한 컨테이너명

app = Flask(__name__)

# DB root 비밀번호 로드
root_password = None
with open('/run/secrets/db-password') as f:
    root_password = f.read()

# 데이터베이스 연동 코드 추가해서, 도커 컴포즈로 구성된 컨테이너간 DB 연동이 잘 되는지 확인
def db_init():
    try:
        # mysql -u root -p
        # password:
        connection = my.connect(host        = 'db',  
                                port        = 3306,         
                                user        = 'root',       
                                password    = root_password,
                                charset     = 'utf8'
                                )
        # mysql[None]:
        with connection: # 커넥션이 with문을 나가면 자동으로 닫힌다
            with connection.cursor() as cur: # 커서는 with문을 나가면 자동으로 닫힌다
                # 1. 데이터베이스 생성
                cur.execute('create database if not EXISTS ml_db;')
                # 2. 커밋 -> 데이터베이스(물리적)에 변동을 가하면(db 생성, 테이블 생성, 데이터 입력/수정/삭제) 확정을 짓는것
                connection.commit()
                # 3. 데이터베이스 사용 지정
                cur.execute('use ml_db;')
                # 4. 테이블 생성
                cur.execute('''
                    create table if not EXISTS dummy (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        title VARCHAR(256)
                    );
                ''')
                # 5. 커밋
                connection.commit()
    except Exception as e:
        print('접속오류', e)

db_init()

# 더미 데이터 삽입 및 조회
def db_insert_select():
    rows = []
    try:
        # 커넥션
        connection = my.connect(host        = 'db',  
                                port        = 3306,         
                                user        = 'root',       
                                password    = root_password,
                                database    = 'ml_db',
                                charset     = 'utf8',
                                cursorclass = my.cursors.DictCursor
                                )
        with connection:
            with connection.cursor() as cur:
                # 더미 데이터 삽입
                cur.execute("insert into dummy (title) VALUES ('test')")
                # 커밋
                connection.commit()
                # 모든 데이터 조회
                cur.execute('select title from dummy')
                # 조회 데이터 획득
                rows = cur.fetchall()
    except Exception as e:
        print( e )
    # 응답
    finally:
        return rows

@app.route('/')
def home():
    rows = db_insert_select()
    return f"Hello Container - 데이터수:{len(rows)}"