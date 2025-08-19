# 🌱 Smart Environment Control System

<table>
  <tr>
    <td width="50%">
      <strong>LED 상태 표시</strong><br>
      <img src="led_status.png" alt="LED Status Display">
    </td>
    <td width="50%">
      <strong>시스템 플로우차트</strong><br>
      <img src="system_flowchart.png" alt="System Flowchart">
    </td>
  </tr>
</table>

<div align="center">

**STM32 NUCLEO-F411RE 기반 스마트 환경 제어 시스템**  
*온습도 센서, RGB LED, 도트매트릭스, LCD를 활용한 실시간 환경 모니터링 및 자동 제어*

</div>

---

## 📋 목차
- [🎯 주요 기능](#🎯-주요-기능)
- [🔧 하드웨어 구성](#🔧-하드웨어-구성)
- [📟 핀 구성](#📟-핀-구성)
- [🎨 RGB LED 상태](#🎨-rgb-led-상태)
- [😊 도트매트릭스 애니메이션](#😊-도트매트릭스-애니메이션)
- [📊 시스템 제어 로직](#📊-시스템-제어-로직)
- [🚀 설치 및 실행](#🚀-설치-및-실행)
- [⚙️ 설정](#⚙️-설정)
- [🔧 문제해결](#🔧-문제해결)
- [🤝 기여하기](#🤝-기여하기)
- [📞 연락처](#📞-연락처)

---

## 🎯 주요 기능

### 🌡️ 환경 모니터링
- **온도 센서**: DHT11 × 2 (실내·실외)
- **습도 센서**: 실시간 습도 모니터링
- **LCD 실시간 표시**: 현재 온습도 상태
- **라즈베리파이 연동**: UART 통신으로 데이터 전송

### 🎨 시각적 피드백
- **RGB LED**: 7 가지 색상으로 환경 상태 표현
- **도트매트릭스**: 8 가지 표정, 2-프레임 반복 애니메이션

### 🔄 스마트 자동 제어
- **팬 제어**: 25 °C / 20 °C 기준
- **가습기 제어**: 55 % / 40 % 기준
- **통합 로직**: 온·습도 조합별 최적 동작

---

## 🔧 하드웨어 구성

| 구성품 | 모델 | 수량 | 비고 |
|--------|------|------|------|
| MCU | STM32 NUCLEO-F411RE | 1 | 메인보드 |
| 온습도 센서 | **DHT11** | 2 | Indoor / Outdoor |
| RGB LED |   | 1 | 공통 캐소드 |
| 8×8 도트매트릭스 | + 74HC595 | 1 | 애니메이션 표시 |
| LCD | I²C 16×2 | 1 | 상태 표시 |
| 가습기 모듈 | 릴레이 방식 | 1 | PC8 제어 |
| 통신 | HC-06 (BLE) | 1 | PC6/PC7 |
| 무선 센서 | EZ-R300 | 1 | PA6 입력 |

---

## 📟 핀 구성

| 구성 | 핀 | 기능 | 설명 |
|------|----|------|------|
| **RGB LED** | PC10 | Red   | R 채널 |
|              | PC11 | Green | G 채널 |
|              | PC12 | Blue  | B 채널 |
| **DHT11**    | PD2  | Indoor  | 실내 센서 |
|              | PC4  | Outdoor | 실외 센서 |
| **Dot-Matrix** | PC1 | SER   | 데이터 입력 |
|                | PC2 | SRCLK | 시프트 클록 |
|                | PC3 | RCLK  | 래치 클록 |
| **LCD (I²C)** | PB6 | SCL | 클록 |
|               | PB7 | SDA | 데이터 |
| **Humidifier** | PC8 | Output | 릴레이 |
| **HC-06**    | PC6 | TX | UART TX |
|              | PC7 | RX | UART RX |
| **EZ-R300**  | PA6 | IN+ | 아날로그 입력 |

---

## 🎨 RGB LED 상태

| RGB 색상 | 조건 | 팬 | 가습기 | 의미 |
|----------|------|----|--------|------|
| 🟡 Yellow | T ≥ 25 °C ∧ H > 55 % | OFF | OFF | 고온 고습 |
| 🔴 Red    | T ≥ 25 °C ∧ H ≤ 55 % | OFF | ON/OFF | 고온 |
| 🟢 Green  | 20 °C ≤ T < 25 °C ∧ H > 55 % | OFF | OFF | 고습 |
| ⚪ White  | 20 °C ≤ T < 25 °C ∧ 40 % < H ≤ 55 % | OFF | OFF | 최적 |
| ⚫ Off    | 20 °C ≤ T < 25 °C ∧ H ≤ 40 % | OFF | ON | 건조 |
| 🟦 Teal   | T < 20 °C ∧ H > 55 % | ON  | OFF | 저온 고습 |
| 🔵 Blue   | T < 20 °C ∧ 40 % < H ≤ 55 % | ON  | OFF | 저온 |

---

## 😊 도트매트릭스 애니메이션

| 애니메이션 | 표시 조건 | 설명 |
|------------|-----------|------|
| **Heat + Dehumi** | 고온·고습 | 땀 + 제습 아이콘 |
| **Heat** | 고온 | 땀 방울 |
| **Heat + Humi** | 고온·건조 | 갈증 표정 |
| **Dehumi** | 고습 | 제습 아이콘 |
| **Smile** | 최적 | 행복 😊 |
| **Humi** | 건조 | 목마름 😮‍💨 |
| **Fan + Dehumi** | 저온·고습 | 바람 + 제습 |
| **Fan** | 저온 | 추위 🥶 |
| **Fan + Humi** | 저온·건조 | 추위 + 갈증 |

*모든 애니메이션은 2 프레임, 500 ms 간격으로 반복됩니다.*

---

## 📊 시스템 제어 로직

flowchart TD
Start --> Read[DHT READ]
Read -- No --> ErrUART[UART "Error"] --> LCDErr[LCD "IN=Error\nOUT=Error"] --> Off[Animation & GPIO OFF]
Read -- Yes --> SendRasPi[UART SEND Temp,Hum] --> CheckT{Temp ≥ 25 °C?}
CheckT -- Yes --> CheckH1{Hum > 55%?}
CheckH1 -- Yes --> LCD1[LCD & Actions] --> Yellow[RGB Yellow / LED Heat+Dehumi]
CheckH1 -- No --> CheckH1b{Hum > 40%?}
CheckH1b -- Yes --> Red1[RGB Red / LED Heat]
CheckH1b -- No --> Red2[RGB Red / LED Heat+Humi]
CheckT -- No --> MidT{Temp ≥ 20 °C?}
MidT -- Yes --> CheckH2{Hum > 55%?}
CheckH2 -- Yes --> Green[RGB Green / LED Dehumi]
CheckH2 -- No --> CheckH2b{Hum > 40%?}
CheckH2b -- Yes --> White[RGB White / LED Smile]
CheckH2b -- No --> OffRGB[RGB Off / LED Humi]
MidT -- No --> CheckH3{Hum > 55%?}
CheckH3 -- Yes --> Teal1[RGB Teal / LED Fan+Dehumi]
CheckH3 -- No --> CheckH3b{Hum > 40%?}
CheckH3b -- Yes --> Blue[RGB Blue / LED Fan]
CheckH3b -- No --> Teal2[RGB Teal / LED Fan+Humi]

text

---

## 🚀 설치 및 실행

1. **필수 도구**  
   - STM32CubeIDE 또는 Keil uVision  
   - STM32 HAL 라이브러리  
   - **DHT11** 드라이버

2. **저장소 클론**  
git clone https://github.com/juntaek-oh/Smart-ENV_control-system.git
cd Smart-ENV_control-system

text

3. **STM32CubeIDE**로 프로젝트 열기 → 핀 설정 확인 → 빌드 & 업로드

---

## ⚙️ 설정

/* 임계값 */
#define TEMP_HIGH 25 // 고온
#define TEMP_MID 20 // 중간
#define HUMI_HIGH 55 // 고습
#define HUMI_MID 40 // 중간

/* 도트매트릭스 */
#define FRAME_DELAY 500 // ms
#define FRAME_CNT 2

text

---

## 🔧 문제해결

| 증상 | 원인 & 해결 |
|------|-------------|
| 센서 값 0 / NaN | DHT11 배선·전원·타이밍 확인 |
| RGB 색상 이상 | PWM 채널·공통 캐소드 배선 확인 |
| 도트매트릭스 깜빡임 | SRCLK/RCLK 신호 확인, 딜레이 조정 |
| LCD 미표시 | I²C 주소·풀업 저항·SCL/SDA 배선 점검 |

---

## 🤝 기여하기

1. **Fork** → 2. **브랜치** 생성 → 3. **커밋** → 4. **푸시** → 5. **Pull Request**

버그·개선 제안은 Issues 탭에 다음 정보를 포함해 주세요.  
OS / IDE 버전 / 보드·센서 모델 / 로그·에러 메시지 / 재현 단계

---

## 📞 연락처

- 📧 ojt8416@gmail.com  
- 💬 [GitHub Issues](https://github.com/juntaek-oh/Smart-ENV_control-system/issues)

---

<div align="center">

🌱 **스마트 환경 제어로 쾌적한 실내 환경을 만들어 보세요!**  
**7 가지 RGB 상태 × 8 가지 도트매트릭스 애니메이션 = 직관적 시각 피드백**

⭐ 도움이 되셨다면 **Star** 부탁드립니다!  
🔄 Pull Request·Issue 대환영!

</div>
