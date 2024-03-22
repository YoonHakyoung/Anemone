import pymysql

try:
    # 데이터베이스 연결 설정
    conn = pymysql.connect(host='localhost',
                           user='root',  # 사용자 이름
                           password='test123',  # 비밀번호
                           database='mydatabase')  # 데이터베이스 이름

    # 커서 생성
    cursor = conn.cursor()

    # 테이블 생성 쿼리
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS events (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        CODENAME VARCHAR(255),
        GUNAME VARCHAR(255),
        TITLE VARCHAR(255),
        DATE VARCHAR(50),
        PLACE VARCHAR(255),
        ORG_NAME VARCHAR(255),
        USE_TRGT TEXT,
        USE_FEE VARCHAR(255),
        MAIN_IMG VARCHAR(255),
        RGSTDATE DATE,
        STRTDATE DATETIME,
        END_DATE DATETIME,
        LOT DECIMAL(10, 8),
        LAT DECIMAL(10, 8),
        IS_FREE VARCHAR(50),
        HMPG_ADDR VARCHAR(255)
    );
    '''

    # 테이블 생성
    cursor.execute(create_table_query)

    # 변경사항 저장
    conn.commit()

except pymysql.Error as e:
    print(f"Error: {e}")

finally:
    # 연결 종료
    if conn:
        conn.close()
