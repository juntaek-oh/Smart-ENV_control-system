# 🌱 스마트 환경 제어 시스템

<div align="center">
  <table>
    <tr>
      <td width="25%">
        <strong>예시 1</strong><br>
        <img src="![시연영상](https://github.com/user-attachments/assets/345c49f8-79cc-4924-a3d0-09f867352a4a)" alt="예시 1" >
      </td>
      <td width="25%">
        <strong>예시 2</strong><br>
        <img src="![시연영상 (1)](https://github.com/user-attachments/assets/111baabe-8cf1-49e2-a425-d71fd09a8686)" alt="예시 2">
      </td>
      <td width="25%">
        <strong>예시 3</strong><br>
        <img src="![시연영상 (2)](https://github.com/user-attachments/assets/fa0bb789-046c-4c60-8aa5-55ab0a248762)" alt="예시 3">
      </td>
      <td width="25%">
        <strong>예시 4 </strong><br>
        <img src="![시연영상 (3)](https://github.com/user-attachments/assets/f54a0976-d4c7-4a3f-a2a2-951c2dc5adf0)" alt="예시 4">
      </td>
    </tr>
  </table>

  <strong>STM32 NUCLEO-F411RE 기반 스마트 환경 제어 시스템</strong><br>
  <em>온습도 센서, RGB LED, 도트매트릭스, LCD를 활용한 실시간 환경 모니터링 및 자동 제어</em>
</div>

## 📋 목차
- [🎯 주요 기능](#-주요-기능)
- [🏗️ 시스템 아키텍처](#-시스템-아키텍처)
- [🔧 하드웨어 구성](#-하드웨어-구성)
- [📟 핀 구성](#-핀-구성)
- [🎨 RGB LED 상태](#-rgb-led-상태)
- [😊 도트매트릭스 애니메이션](#-도트매트릭스-애니메이션)
- [📊 시스템 제어 로직](#-시스템-제어-로직)
- [🚀 설치 및 실행](#-설치-및-실행)
- [⚙️ 설정](#-설정)
- [🔧 문제해결](#-문제해결)
- [🤝 기여하기](#-기여하기)

## 🎯 주요 기능

### 🌡️ 실시간 환경 모니터링
- **온도 및 습도 센서**: DHT11 x2 (실내/실외)로 온습도 측정
- **실시간 표시**: LCD 1602에 실시간 온습도 표시
- **데이터 수집**: 1분 간격으로 데이터 수집 및 MySQL 저장
- **라즈베리파이 연동**: HC-06 블루투스를 통한 데이터 전송

### 🤖 자동 환경 제어
- **온도 제어**: 내부 온도 > 28°C 시 EZ 모터 R300(선풍기) ON
- **습도 제어**: 내부 습도 < 60% 시 가습기 ON
- **시각적 피드백**:
  - RGB LED: 3가지 색상 (파랑: ≤15°C, 초록: 16-27°C, 빨강: ≥28°C)
  - 도트매트릭스: 3가지 표정 (😊: 정상, 😐: 주의, ☹️: 제어 활성화)

### 📡 IoT 통신 및 데이터 관리
- **무선 전송**: STM32 → HC-06 → Raspberry Pi
- **데이터베이스**: MySQL에 실내/실외 온습도 저장
- **시각화**: Grafana 대시보드로 실시간 온습도 그래프 제공
- **원격 모니터링**: 웹 기반 상태 확인

### 🛡️ 안정성 및 예외처리
- 센서 오류 및 블루투스 연결 실패 처리
- 전압 모니터링 및 통신 타임아웃 관리

## 🏗️ 시스템 아키텍처
```
graph TB
    subgraph "Sensor Layer"
        A[실내 DHT11<br/>온습도 센서]
        B[실외 DHT11<br/>온습도 센서]
    end
    subgraph "Control Unit"
        C[STM32F411RE<br/>메인 컨트롤러]
        D[LCD 1602<br/>실시간 표시]
        E[8x8 Dot Matrix<br/>상태 표정]
        F[RGB LED<br/>온도 상태]
    end
    subgraph "Actuators"
        G[EZ 모터 R300<br/>선풍기 제어]
        H[가습기 모듈<br/>습도 제어]
    end
    subgraph "Communication Layer"
        I[HC-06<br/>블루투스 모듈]
        J[Raspberry Pi 4<br/>IoT 게이트웨이]
    end
    subgraph "Data & Visualization"
        K[MySQL 데이터베이스<br/>시계열 데이터 저장]
        L[Grafana 대시보드<br/>실시간 시각화]
        M[웹 인터페이스<br/>원격 모니터링]
    end
    A --> C
    B --> C
    C --> D
    C --> E
    C --> F
    C --> G
    C --> H
    C --> I --> J
    J --> K --> L
    L --> M
```

## 🔧 하드웨어 구성
- **메인보드**: STM32F411RE
- **온습도 센서**: DHT11 x2 (실내/실외)
- **디스플레이**: LCD 1602, 8x8 도트매트릭스 (74HC595 시프트 레지스터), RGB LED (공통 캐소드)
- **액추에이터**: EZ 모터 R300 (선풍기), 가습기 모듈 (릴레이 제어)
- **통신**: HC-06 블루투스, Raspberry Pi 4

## 📟 핀 구성
| 구성요소       | 핀 번호    | 기능     | 설명                     |
|----------------|------------|----------|--------------------------|
| 실내 DHT11     | PA0        | 데이터   | 실내 온습도 센서         |
| 실외 DHT11     | PA1        | 데이터   | 실외 온습도 센서         |
| LCD 1602       | PB12-PB15  | D4-D7    | 데이터 버스              |
|                | PB10       | RS       | 레지스터 선택            |
|                | PB11       | E        | 활성화 신호              |
| 도트매트릭스   | PC1        | SER      | 직렬 데이터 입력         |
|                | PC2        | SRCLK    | 시프트 레지스터 클록     |
|                | PC3        | RCLK     | 래치 클록                |
| RGB LED        | PA8        | Red      | 빨간색 LED 제어          |
|                | PA9        | Green    | 초록색 LED 제어          |
|                | PA10       | Blue     | 파란색 LED 제어          |
| EZ 모터 R300   | PB0        | PWM      | 선풍기 제어              |
| 가습기         | PB1        | 릴레이   | 가습기 제어              |
| HC-06          | PA2        | TX       | 블루투스 송신            |
|                | PA3        | RX       | 블루투스 수신            |

## 🎨 RGB LED 상태
| LED 색상 | 온도 범위 | 의미         |
|----------|-----------|--------------|
| 🔵 파란색 | ≤15°C     | 낮은 온도    |
| 🟢 초록색 | 16-27°C   | 적정 온도    |
| 🔴 빨간색 | ≥28°C     | 높은 온도    |

## 😊 도트매트릭스 애니메이션
| 표정 | 온도 조건   | 제어 상태       |
|------|-------------|-----------------|
| 😊   | 적정 온도   | 정상            |
| 😐   | 경계 온도   | 주의            |
| ☹️   | 임계 초과   | 제어 작동       |

### 애니메이션 특징
- 500ms 간격으로 프레임 전환
- 무한 반복 애니메이션
- 상황별 표정으로 직관적 상태 표현

## 📊 시스템 제어 로직
```
시작 → DHT11 센서 읽기
  ↓
센서 오류? → UART "Error" 전송 → LCD "Error" 표시 → 애니메이션 OFF
  ↓
정상 읽기 → 라즈베리파이 데이터 전송 → MySQL 저장
  ↓
온도 > 28°C?
├─ YES → 선풍기 ON, RGB=Red, 도트매트릭스=☹28
└─ NO → 온도 > 15°C?
    ├─ YES → 선풍기 OFF, RGB=Green, 도트매트릭스=😊
    └─ NO → 선풍기 OFF, RGB=Blue, 도트매트릭스=😐
  ↓
습도 < 60%?
├─ YES → 가습기 ON
└─ NO → 가습기 OFF
```

## 🚀 설치 및 실행

### 필수 사항
- STM32CubeIDE 또는 Keil uVision
- STM32 HAL 라이브러리
- DHT11 라이브러리
- Raspberry Pi 4, Python 3.9+, MySQL 8.0, Grafana 8.0+
- 12V/5V/3.3V 전원 공급

### 설치 과정
1. **저장소 복제**
   ```bash
   git clone https://github.com/juntaek-oh/Smart-ENV_control-system.git
   cd Smart-ENV_control-system
   ```
2. **STM32 펌웨어 업로드**
   ```bash
   st-flash write build/smart_barn.bin 0x8000000
   ```
3. **Raspberry Pi 설정**
   ```bash
   sudo apt-get update
   sudo apt-get install python3-pip python3-venv
   python3 -m venv venv
   source venv/bin/activate
   pip install pyserial mysql-connector-python configparser
   ```
4. **MySQL 설정**
   ```sql
   CREATE DATABASE smart_barn;
   USE smart_barn;
   CREATE TABLE environmental_data (
       id INT AUTO_INCREMENT PRIMARY KEY,
       timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
       indoor_temp FLOAT NOT NULL,
       indoor_humidity FLOAT NOT NULL,
       outdoor_temp FLOAT NOT NULL,
       outdoor_humidity FLOAT NOT NULL,
       fan_status BOOLEAN DEFAULT FALSE,
       humidifier_status BOOLEAN DEFAULT FALSE
   );
   ```
5. **Grafana 설치**
   ```bash
   sudo apt-get install -y software-properties-common
   sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"
   sudo apt-get update
   sudo apt-get install grafana
   sudo systemctl start grafana-server
   sudo systemctl enable grafana-server
   ```

### 실행
```bash
source venv/bin/activate
python RaspberryPi/data_receiver.py
sudo systemctl start smart-barn.service
```

## ⚙️ 설정
### 임계값 설정 (`config.json`)
```json
{
  "thresholds": {
    "max_temp": 28.0,
    "min_temp": 15.0,
    "min_humidity": 60.0,
    "max_humidity": 85.0
  },
  "control_settings": {
    "fan_delay": 30,
    "humidifier_delay": 60,
    "data_interval": 60
  }
}
```

### 통신 설정
```json
{
  "bluetooth": {
    "device_address": "98:D3:32:31:59:26",
    "auto_reconnect": true,
    "reconnect_interval": 10,
    "timeout": 5
  }
}
```

## 🔧 문제해결
- **블루투스 연결 실패**:
  - HC-06 전원 및 페어링 확인:
    ```bash
    sudo hcitool scan
    sudo bluetoothctl
    pair 98:D3:32:31:59:26
    sudo rfcomm bind 0 98:D3:32:31:59:26
    ```
- **센서 읽기 실패**:
  - VCC/GND/데이터 핀 연결 확인
  - 10kΩ 풀업 저항 확인
  - 5초 이상 간격으로 센서 읽기
- **MySQL 연결 오류**:
  - 서비스 상태 확인:
    ```bash
    sudo systemctl status mysql
    ```
  - 사용자 권한:
    ```sql
    GRANT ALL PRIVILEGES ON smart_barn.* TO 'smart_barn'@'localhost';
    FLUSH PRIVILEGES;
    ```
  - 방화벽:
    ```bash
    sudo ufw allow 3306
    ```
- **Grafana 표시 문제**:
  - 데이터소스, 쿼리, 시간 범위, 필드 매핑 확인

## 🤝 기여하기
### 기여 방법
1. Fork the Project
2. Create Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to Branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

### 🐛 버그 리포트
Issues 탭에서 다음 정보를 제공:
- **하드웨어**: STM32 보드, 센서 모델
- **개발환경**: STM32CubeIDE 버전, HAL 라이브러리, Python 버전
- **에러 메시지**: 컴파일/런타임 에러
- **재현 단계**: 문제 발생 절차
- **기대/실제 동작**

### 📞 연락처
- **이메일**: ojt8416@gmail.com
- **GitHub Issues**: [링크](#)

<div align="center">
  🌱 스마트 환경 제어로 쾌적한 축사 환경을 만들어보세요!<br>
  STM32와 IoT 기술로 구현한 지능형 환경 제어 시스템<br>
  ⭐ 도움이 되셨다면 Star를 눌러주세요! ⭐<br>
  🔄 Pull Requests와 Issues를 환영합니다!
</div>
