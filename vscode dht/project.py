from flask import Flask, render_template, jsonify
import mysql.connector
from datetime import datetime
import threading
import serial
import time

app = Flask(__name__)

# DB 설정
db_config = {
    'host': "10.10.10.117",
    'user': "root",
    'passwd': "1234",
    'database': "DHT11_db",
    'port': 3306
}

# 데이터베이스 연결 함수
def connect_db():
    try:
        conn = mysql.connector.connect(**db_config)
        print("✅ DB 연결 성공")
        return conn
    except mysql.connector.Error as e:
        print(f"❌ DB 연결 실패: {e}")
        return None

# 실시간 데이터 수집 함수 (센서 → DB)
def sensor_worker():
    # 데이터베이스 연결
    Maria = connect_db()
    if not Maria:
        return
    Cursor = Maria.cursor()

    # 시리얼 포트 설정
    try:
        ser = serial.Serial('/dev/rfcomm0', 9600, timeout=10)
        print("✅ 시리얼 포트 열림")
        time.sleep(2)  # 연결 안정화 대기
    except serial.SerialException as e:
        print(f"❌ 포트 열기 실패: {e}")
        Cursor.close()
        Maria.close()
        return

    buffer = ""  # 시리얼 데이터 버퍼
    try:
        while True:
            # 데이터베이스 연결 확인 및 재연결
            if not Maria.is_connected():
                print("🔄 DB 연결 끊김, 재연결 시도")
                Cursor.close()
                Maria.close()
                Maria = connect_db()
                if not Maria:
                    time.sleep(5)
                    continue
                Cursor = Maria.cursor()

            # 시리얼 데이터 읽기
            buffer += ser.read(ser.in_waiting or 1).decode(errors='ignore')
            if '\n' in buffer:
                lines = buffer.split('\n')
                buffer = lines[-1]  # 마지막 (미완성) 줄은 버퍼에 저장
                for line in lines[:-1]:
                    line = line.strip()
                    if not line:
                        continue
                    print(f"📥 받은 데이터: {repr(line)}")

                    # DHT10 데이터 (IN: temp,hum)
                    if "IN:" in line:
                        try:
                            parts = line.split(",")
                            if len(parts) != 2:
                                raise ValueError("잘못된 데이터 형식")
                            temperature_in = int(parts[0].split(":")[1].strip())
                            humidity_in = int(parts[1].strip())
                            Cursor.execute(
                                "INSERT INTO sensor_data (humidity_in, temperature_in, timestamp) VALUES (%s, %s, %s)",
                                (humidity_in, temperature_in, datetime.now())
                            )
                            Maria.commit()
                            print(f"🌡️ temperature_in: {temperature_in}°C, 💧 humidity_in: {humidity_in}% 저장됨")
                        except Exception as e:
                            print(f"⚠️ DHT10 파싱 오류: {e}, 데이터: {repr(line)}")
                    # DHT11 데이터 (OUT: temp,hum)
                    elif "OUT:" in line:
                        try:
                            parts = line.split(",")
                            if len(parts) != 2:
                                raise ValueError("잘못된 데이터 형식")
                            temperature_out = int(parts[0].split(":")[1].strip())
                            humidity_out = int(parts[1].strip())
                            Cursor.execute(
                                "INSERT INTO sensor_data_out (humidity_out, temperature_out, timestamp) VALUES (%s, %s, %s)",
                                (humidity_out, temperature_out, datetime.now())
                            )
                            Maria.commit()
                            print(f"🌡️ temperature_out: {temperature_out}°C, 💧 humidity_out: {humidity_out}% 저장됨")
                        except Exception as e:
                            print(f"⚠️ DHT11 파싱 오류: {e}, 데이터: {repr(line)}")
                    else:
                        print(f"⚠️ 무시된 데이터: {repr(line)}")

                    # 데이터 개수 관리 (50개 제한)
                    Cursor.execute("SELECT COUNT(*) FROM sensor_data")
                    count_in = Cursor.fetchone()[0]
                    if count_in >= 50:
                        Cursor.execute("DELETE FROM sensor_data ORDER BY timestamp ASC LIMIT 1")
                        Maria.commit()
                        print("✅ sensor_data 오래된 데이터 1개 삭제")

                    Cursor.execute("SELECT COUNT(*) FROM sensor_data_out")
                    count_out = Cursor.fetchone()[0]
                    if count_out >= 50:
                        Cursor.execute("DELETE FROM sensor_data_out ORDER BY timestamp ASC LIMIT 1")
                        Maria.commit()
                        print("✅ sensor_data_out 오래된 데이터 1개 삭제")

            time.sleep(0.01)  # 빠른 폴링
    except KeyboardInterrupt:
        print("🛑 종료 요청 받음")
    finally:
        ser.close()
        Cursor.close()
        Maria.close()
        print("🔒 리소스 정리 완료")

# Flask 라우터
@app.route('/')
def index():
    return render_template('two.html')

@app.route('/data')
def data():
    db = connect_db()
    if not db:
        return jsonify({'error': '❌ DB 연결 실패'}), 500

    cursor1 = db.cursor()
    cursor2 = db.cursor()
    result = {}

    # 최신 DHT10 데이터 가져오기
    cursor1.execute("SELECT temperature_in, humidity_in, timestamp FROM sensor_data ORDER BY timestamp DESC LIMIT 1")
    row1 = cursor1.fetchone()
    if row1:
        result.update({
            'temperature_in': row1[0],
            'humidity_in': row1[1],
            'time_in': row1[2].strftime('%H:%M:%S')
        })

    # 최신 DHT11 데이터 가져오기
    cursor2.execute("SELECT temperature_out, humidity_out, timestamp FROM sensor_data_out ORDER BY timestamp DESC LIMIT 1")
    row2 = cursor2.fetchone()
    if row2:
        result.update({
            'temperature_out': row2[0],
            'humidity_out': row2[1]
        })

    cursor1.close()
    cursor2.close()
    db.close()

    if not result:
        return jsonify({'error': '❌ 센서 데이터가 없습니다'}), 404

    return jsonify(result)

# 메인 실행
if __name__ == '__main__':
    sensor_thread = threading.Thread(target=sensor_worker, daemon=True)
    sensor_thread.start()
    app.run(host='0.0.0.0', port=5000, debug=False)