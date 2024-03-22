import requests
import sys
import json
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
        DATE VARCHAR(255),
        PLACE VARCHAR(255),
        ORG_NAME VARCHAR(255),
        USE_TRGT VARCHAR(255),
        USE_FEE VARCHAR(255),
        PLAYER TEXT,
        PROGRAM TEXT,
        ETC_DESC TEXT,
        ORG_LINK VARCHAR(255),
        MAIN_IMG VARCHAR(255),
        RGSTDATE DATE,
        STRTDATE DATETIME,
        END_DATE DATETIME,
        LOT DECIMAL(10, 8),
        LAT DECIMAL(11, 8),
        IS_FREE VARCHAR(50),
        HMPG_ADDR VARCHAR(255),
        TICKET VARCHAR(255)
    );
    '''

    # 테이블 생성
    cursor.execute(create_table_query)

    # API
    url = "http://openapi.seoul.go.kr:8088/7a7a456a7879686b313030514d69784a/json/culturalEventInfo/1/1000/"

    response = requests.get(url)
    sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8')

    # utf-8 인코딩 -> json -> 필요한 값 들어있는 리스트만
    result = json.loads(response.content.decode('utf-8'))['culturalEventInfo']['row']

    for i in result:
        CODENAME = i['CODENAME']
        GUNAME = i['GUNAME']
        TITLE = i['TITLE']
        DATE = i['DATE']
        PLACE = i['PLACE']
        ORG_NAME = i['ORG_NAME']
        USE_TRGT = i['USE_TRGT']
        USE_FEE = i['USE_FEE']
        MAIN_IMG = i['MAIN_IMG']
        RGSTDATE = i['RGSTDATE']
        STRTDATE = i['STRTDATE']
        END_DATE = i['END_DATE']
        LOT = i['LOT']
        LAT = i['LAT']
        IS_FREE = i['IS_FREE']
        HMPG_ADDR = i['HMPG_ADDR']
        PLAYER = i.get('PLAYER', '')  
        PROGRAM = i.get('PROGRAM', '')  
        ETC_DESC = i.get('ETC_DESC', '')  
        ORG_LINK = ""
        TICKET = i['TICKET']

        print(i['USE_FEE'])
        # 데이터 삽입 쿼리
        insert_query = '''
        INSERT INTO events (CODENAME, GUNAME, TITLE, DATE, PLACE, ORG_NAME, USE_TRGT, USE_FEE, MAIN_IMG, RGSTDATE, STRTDATE, END_DATE, LOT, LAT, IS_FREE, HMPG_ADDR, PLAYER, PROGRAM, ETC_DESC, ORG_LINK, TICKET)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(insert_query, (CODENAME, GUNAME, TITLE, DATE, PLACE, ORG_NAME, USE_TRGT, USE_FEE, MAIN_IMG, RGSTDATE, STRTDATE, END_DATE, LOT, LAT, IS_FREE, HMPG_ADDR, PLAYER, PROGRAM, ETC_DESC, ORG_LINK, TICKET))


    # 변경사항 저장
    conn.commit()

except pymysql.Error as e:
    print(f"Error: {e}")

finally:
    # 연결 종료
    if conn:
        conn.close()