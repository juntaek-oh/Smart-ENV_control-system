# 🌱 스마트 환경 제어 시스템

<table>
<tr>
<td width="25%">

![시연영상](https://github.com/user-attachments/assets/c185b752-f42f-4306-9656-85c974743606)


</td>

<td width="25%">

![시연영상 (1)](https://github.com/user-attachments/assets/7b4c1000-8b78-4675-91f6-d40c16e2b0cd)

</td>

<td width="25%">

![시연영상 (2)](https://github.com/user-attachments/assets/b3c3917e-4d8d-4ad6-a457-a77fd989651c)

</td>

<td width="25%">

![시연영상 (3)](https://github.com/user-attachments/assets/a4d9d83d-6971-4071-93dc-610983fc5a29)

</td>
</tr>
</table>

  <strong>STM32 NUCLEO-F411RE 기반 스마트 축사 환경 제어 시스템</strong><br>
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

### 🌡️ 환경 모니터링
- **온도 센서**: DHT11를 활용한 실내외 온도 측정
- **습도 센서**: 실시간 습도 모니터링 및 제어
- **실시간 표시**: LCD 16x2에 현재 온습도 상태 표시
- **라즈베리파이 연동**: UART를 통해 데이터 전송, MySQL 저장, Grafana로 시각화

### 🎨 시각적 피드백 시스템
- **다양한 RGB LED 색상**: 7가지 색상으로 환경 상태 표현
- **도트매트릭스 애니메이션**: 8가지 표정으로 감정 표현, 2프레임 반복
- **실시간 표시**: LCD에 온습도 및 상태 표시

### 🔄 스마트 자동 제어
- **온도별 팬 제어**: 25°C/20°C 기준 단계별 제어
- **습도별 가습기 제어**: 55%/40% 기준 자동 가습
- **통합 환경 제어**: 온습도 조합에 따른 최적 제어

### 📡 IoT 통신 및 데이터 관리
- **무선 전송**: HC-06 블루투스를 통해 STM32에서 Raspberry Pi로 데이터 전송
- **데이터베이스**: MySQL에 실내/실외 온습도 저장
- **시각화**: Grafana 대시보드로 실시간 온습도 그래프 제공
- **원격 모니터링**: 웹 기반 상태 확인

## 🏗️ 시스템 아키텍처
이 시스템은 실내외 환경을 모니터링하고 제어하기 위해 여러 구성 요소가 단계적으로 연결되어 동작합니다. 아래는 시스템의 흐름을 간단히 설명합니다:

1. **센서**: 두 개의 DHT11 센서가 실내와 실외의 온도와 습도를 측정합니다. 이 센서들은 STM32 마이크로컨트롤러에 연결되어 데이터를 제공합니다.
2. **중앙 제어**: STM32 NUCLEO-F411RE 보드가 센서 데이터를 수집하고 처리합니다. STM32는 환경 데이터를 분석하여 팬과 가습기를 제어하고, LCD, RGB LED, 도트매트릭스에 상태를 표시합니다.
3. **상태 표시**: LCD는 실내외 온습도를 실시간으로 보여주고, RGB LED는 온도와 습도 상태를 7가지 색상으로 표현합니다. 도트매트릭스는 환경 상태에 따라 8가지 표정을 애니메이션으로 표시합니다.
4. **액추에이터**: STM32는 온도와 습도에 따라 EZ 모터 R300(선풍기)과 가습기 모듈을 자동으로 켜거나 끕니다.
5. **통신**: STM32는 HC-06 블루투스 모듈을 통해 실시간 데이터를 Raspberry Pi로 전송합니다.
6. **데이터 저장 및 시각화**: Raspberry Pi는 수신한 데이터를 MySQL 데이터베이스에 저장합니다. Grafana는 이 데이터를 가져와 실시간 온습도 그래프와 제어 상태를 웹 대시보드로 표시합니다.
7. **원격 모니터링**: 사용자는 웹 브라우저를 통해 Grafana 대시보드에 접속하여 축사의 환경 상태를 원격으로 확인할 수 있습니다.

이러한 구조로, 시스템은 센서 데이터를 실시간으로 수집, 처리, 표시하고, 환경을 자동 제어하며, IoT 기술로 원격 모니터링을 제공합니다.

## 🔧 하드웨어 구성
- **메인보드**: STM32 NUCLEO-F411RE
- **온습도 센서**: DHT11 × 2 (실내/실외)
- **RGB LED**: 공통 캐소드 타입
- **도트매트릭스**: 8×8 LED Matrix + 74HC595 시프트 레지스터
- **LCD**: 16×2 I2C LCD 모듈
- **가습기 모듈**: 릴레이 제어 방식
- **통신 모듈**: HC-06 블루투스, EZ-R300 무선 모듈, Raspberry Pi 4

## 📟 핀 구성
| 구성요소       | 핀 번호 | 기능     | 설명                     |
|----------------|---------|----------|--------------------------|
| RGB LED        | PC10    | Red      | 빨간색 LED 제어          |
|                | PC11    | Green    | 초록색 LED 제어          |
|                | PC12    | Blue     | 파란색 LED 제어          |
| DHT 센서       | PD2     | Indoor   | 실내 온습도 센서         |
|                | PC4     | Outdoor  | 실외 온습도 센서         |
| 도트매트릭스   | PC1     | SER      | 직렬 데이터 입력         |
|                | PC2     | SRCLK    | 시프트 레지스터 클록     |
|                | PC3     | RCLK     | 래치 클록                |
| LCD            | PB6     | SCL      | I2C 클록 라인            |
|                | PB7     | SDA      | I2C 데이터 라인           |
| 가습기         | PC8     | Output   | 가습기 릴레이 제어       |
| HC-06          | PC6     | TX       | 블루투스 송신            |
|                | PC7     | RX       | 블루투스 수신            |
| EZ-R300        | PA6     | IN+      | 무선 모듈 입력           |

## 🎨 RGB LED 상태
| RGB 색상 | 조건                     | 팬   | 가습기   | 의미                     |
|----------|--------------------------|------|----------|--------------------------|
| 🟡 Yellow | 온도 ≥ 25°C, 습도 > 55% | OFF  | OFF      | 고온 고습 - 제습 필요    |
| 🔴 Red   | 온도 ≥ 25°C, 습도 ≤ 55% | OFF  | ON/OFF   | 고온 - 냉각 필요         |
| 🟢 Green | 온도 ≥ 20°C, 습도 > 55% | OFF  | OFF      | 쾌적 온도, 습도 높음     |
| ⚪ White | 온도 ≥ 20°C, 습도 40-55% | OFF  | OFF      | 최적 환경 상태           |
| ⚫ Off   | 온도 ≥ 20°C, 습도 ≤ 40% | OFF  | ON       | 건조 환경                |
| 🔵 Teal  | 온도 < 20°C, 습도 > 55% | ON   | OFF      | 저온 고습                |
| 🔵 Blue  | 온도 < 20°C, 습도 40-55% | ON   | OFF      | 저온 환경                |

## 😊 도트매트릭스 애니메이션
| 애니메이션       | 표시 조건     | 설명                          |
|------------------|---------------|-------------------------------|
| Heat, Dehumi     | 고온 고습     | 더위 + 제습 표정 (2프레임 반복) |
| Heat             | 고온 상태     | 더위 표정 (땀 애니메이션)      |
| Heat, Humi       | 고온 건조     | 더위 + 갈증 표정              |
| Dehumi           | 고습 상태     | 제습 표정 (습기 제거)         |
| Smile            | 최적 환경     | 행복 표정 (미소 애니메이션)    |
| Humi             | 건조 상태     | 목마름 표정                   |
| Fan, Dehumi      | 저온 고습     | 팬 + 제습 표정                |
| Fan              | 저온 상태     | 추위 표정 (바람 효과)         |
| Fan, Humi        | 저온 건조     | 추위 + 갈증 표정              |

### 애니메이션 특징
- 500ms 간격으로 프레임 전환
- 무한 반복 애니메이션
- 상황별 맞춤 표정으로 직관적 상태 표현

## 📊 시스템 제어 로직
```
시작 → DHT11 센서 읽기
  ↓
센서 오류? → UART "Error" 전송 → LCD "Error" 표시 → 애니메이션 OFF
  ↓
정상 읽기 → 라즈베리파이 데이터 전송 → MySQL 저장
  ↓
온도 ≥ 25°C?
├─ YES → 습도 > 55%?
│   ├─ YES → 팬 OFF, 가습기 OFF, RGB=Yellow → LED: Heat,Dehumi
│   └─ NO → 습도 > 40%?
│       ├─ YES → 팬 OFF, 가습기 OFF, RGB=Red → LED: Heat  
│       └─ NO → 팬 OFF, 가습기 ON, RGB=Red → LED: Heat,Humi
└─ NO → 온도 ≥ 20°C?
    ├─ YES → 습도 > 55%?
    │   ├─ YES → 팬 OFF, 가습기 OFF, RGB=Green → LED: Dehumi
    │   └─ NO → 습도 > 40%?
    │       ├─ YES → 팬 OFF, 가습기 OFF, RGB=White → LED: Smile
    │       └─ NO → 팬 OFF, 가습기 ON, RGB=Off → LED: Humi  
    └─ NO → 습도 > 55%?
        ├─ YES → 팬 ON, 가습기 OFF, RGB=Teal → LED: Fan,Dehumi
        └─ NO → 습도 > 40%?
            ├─ YES → 팬 ON, 가습기 OFF, RGB=Blue → LED: Fan
            └─ NO → 팬 ON, 가습기 ON, RGB=Teal → LED: Fan,Humi
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

### 온도 및 습도 임계값 설정 (`config.json`)
```json
{
  "thresholds": {
    "max_temp": 25.0,
    "mid_temp": 20.0,
    "high_humidity": 55.0,
    "mid_humidity": 40.0
  },
  "control_settings": {
    "fan_delay": 30,
    "humidifier_delay": 60,
    "data_interval": 60
  }
}
```

### 애니메이션 설정
```c
#define ANIMATION_FRAME_DELAY 500  // 프레임 전환 주기 (ms)
#define ANIMATION_FRAMES      2    // 프레임 수
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

### 일반적인 문제들
- **센서 읽기 오류**:
  - DHT11 연결 및 전원 공급(VCC, GND) 확인
  - 데이터 핀에 10kΩ 풀업 저항 확인
  - 5초 이상 간격으로 센서 읽기
- **RGB LED 색상 오류**:
  - PWM 설정 및 공통 캐소드 연결 확인
- **도트매트릭스 깜빡임**:
  - 시프트 레지스터 클록 신호(SRCLK, RCLK) 점검
- **LCD I2C 통신 오류**:
  - SCL/SDA 풀업 저항 확인
- **블루투스 연결 실패**:
  - HC-06 전원 및 페어링 확인:
    ```bash
    sudo hcitool scan
    sudo bluetoothctl
    pair 98:D3:32:31:59:26
    sudo rfcomm bind 0 98:D3:32:31:59:26
    ```
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

### 📝 기여 방법
1. Fork the Project
2. Create Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to Branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

### 🐛 버그 리포트
Issues 탭에서 다음 정보를 제공:
- **하드웨어**: STM32 보드 모델, 센서 모델 등
- **개발환경**: STM32CubeIDE 버전, HAL 라이브러리, Python 버전
- **에러 메시지**: 컴파일 에러 또는 런타임 에러
- **재현 단계**: 문제 발생 상황 및 절차
- **기대 동작**: 예상했던 결과
- **실제 동작**: 실제 발생한 결과

### 📞 연락처
- **이메일**: ojt8416@gmail.com
- **GitHub Issues**: [링크](#)

<div align="center">
  🌱 스마트 환경 제어로 쾌적한 축사 환경을 만들어보세요!<br>
  STM32와 IoT 기술로 구현한 지능형 환경 제어 시스템<br>
  7가지 RGB 상태 × 8가지 도트매트릭스 애니메이션 = 직관적 상태 표현<br><br>
  ⭐ 도움이 되셨다면 Star를 눌러주세요! ⭐<br>
  🔄 Pull Requests와 Issues를 환영합니다!
</div>
