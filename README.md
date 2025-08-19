스마트 환경 제어 시스템

  
    
      LED 상태 표시
      
    
    
      시스템 플로우차트
      
    
  



  STM32 NUCLEO-F411RE 기반 스마트 환경 제어 시스템
  온습도 센서, RGB LED, 도트매트릭스, LCD를 활용한 실시간 환경 모니터링 및 자동 제어


📋 목차

🎯 주요 기능
🔧 하드웨어 구성
📟 핀 구성
🎨 RGB LED 상태
😊 도트매트릭스 애니메이션
📊 시스템 제어 로직
🚀 설치 및 실행
⚙️ 설정
🔧 문제해결
🤝 기여하기

🎯 주요 기능
🌡️ 환경 모니터링

온도 센서: DHT11를 활용한 실내외 온도 측정
습도 센서: 실시간 습도 모니터링 및 제어
실시간 표시: LCD를 통한 현재 온습도 상태 표시
라즈베리파이 연동: UART 통신으로 데이터 전송

🎨 시각적 피드백 시스템

다양한 RGB LED 색상: 7가지 색상으로 환경 상태 표현
도트매트릭스 애니메이션: 8가지 표정으로 감정 표현
반복 애니메이션: 각 표정마다 2프레임 순환 재생

🔄 스마트 자동 제어

온도별 팬 제어: 25°C/20°C 기준 단계별 제어
습도별 가습기 제어: 55%/40% 기준 자동 가습
통합 환경 제어: 온습도 조합에 따른 최적 제어

🔧 하드웨어 구성

메인보드: STM32 NUCLEO-F411RE
온습도 센서: DHT11 × 2 (실내/실외)
RGB LED: 공통 캐소드 타입
도트매트릭스: 8×8 LED Matrix + 74HC595 시프트 레지스터
LCD: 16×2 I2C LCD 모듈
가습기 모듈: 릴레이 제어 방식
통신 모듈: HC-06 블루투스, EZ-R300 무선 모듈

📟 핀 구성



구성요소
핀 번호
기능
설명



RGB LED
PC10
Red
빨간색 LED 제어



PC11
Green
초록색 LED 제어



PC12
Blue
파란색 LED 제어


DHT 센서
PD2
Indoor
실내 온습도 센서



PC4
Outdoor
실외 온습도 센서


도트매트릭스
PC1
SER
직렬 데이터 입력



PC2
SRCLK
시프트 레지스터 클록



PC3
RCLK
래치 클록


LCD
PB6
SCL
I2C 클록 라인



PB7
SDA
I2C 데이터 라인


가습기
PC8
Output
가습기 릴레이 제어


HC-06
PC6
TX
블루투스 송신



PC7
RX
블루투스 수신


EZ-R300
PA6
IN+
무선 모듈 입력


🎨 RGB LED 상태
플로우차트 기반 7가지 RGB 색상 상태:



RGB 색상
조건
팬
가습기
의미



🟡 Yellow
온도 ≥ 25°C, 습도 > 55%
OFF
OFF
고온 고습 - 제습 필요


🔴 Red
온도 ≥ 25°C, 습도 ≤ 55%
OFF
ON/OFF
고온 - 냉각 필요


🟢 Green
온도 ≥ 20°C, 습도 > 55%
OFF
OFF
쾌적 온도, 습도 높음


⚪ White
온도 ≥ 20°C, 습도 40-55%
OFF
OFF
최적 환경 상태


⚫ Off
온도 ≥ 20°C, 습도 ≤ 40%
OFF
ON
건조 환경


🔵 Teal
온도 < 20°C, 습도 > 55%
ON
OFF
저온 고습


🔵 Blue
온도 < 20°C, 습도 40-55%
ON
OFF
저온 환경


😊 도트매트릭스 애니메이션
8가지 표정 애니메이션 (각 2프레임 반복):



애니메이션
표시 조건
설명



Heat, Dehumi
고온 고습
더위 + 제습 표정 (2프레임 반복)


Heat
고온 상태
더위 표정 (땀 애니메이션)


Heat, Humi
고온 건조
더위 + 갈증 표정


Dehumi
고습 상태
제습 표정 (습기 제거)


Smile
최적 환경
행복 표정 (미소 애니메이션)


Humi
건조 상태
목마름 표정


Fan, Dehumi
저온 고습
팬 + 제습 표정


Fan
저온 상태
추위 표정 (바람 효과)


Fan, Humi
저온 건조
추위 + 갈증 표정


애니메이션 특징

500ms 간격으로 프레임 전환
무한 반복 애니메이션
상황별 맞춤 표정으로 직관적 상태 표현

📊 시스템 제어 로직
플로우차트 기반 상세 제어 로직:
시작 → DHT 센서 읽기
  ↓
센서 오류? → UART "Error" 전송 → LCD "Error" 표시 → 애니메이션 OFF
  ↓
정상 읽기 → 라즈베리파이 데이터 전송
  ↓
온도 ≥ 25°C?
├─ YES → 습도 > 55%?
│   ├─ YES → 팬 OFF, 가습기 OFF, RGB=Yellow → LED: Heat,Dehumi
│   └─ NO → 습도 > 40%?
│       ├─ YES → 팬 OFF, 가습기 OFF, RGB=Red → LED: Heat  
│       └─ NO → 팬 OFF, 가습기 ON, RGB=Red → LED: Heat,Humi
│
└─ NO → 온도 ≥ 20°C?
    ├─ YES → 습도 > 55%?
    │   ├─ YES → 팬 OFF, 가습기 OFF, RGB=Green → LED: Dehumi
    │   └─ NO → 습도 > 40%?
    │       ├─ YES → 팬 OFF, 가습기 OFF, RGB=White → LED: Smile
    │       └─ NO → 팬 OFF, 가습기 ON, RGB=Off → LED: Humi  
    │
    └─ NO → 습도 > 55%?
        ├─ YES → 팬 ON, 가습기 OFF, RGB=Teal → LED: Fan,Dehumi
        └─ NO → 습도 > 40%?
            ├─ YES → 팬 ON, 가습기 OFF, RGB=Blue → LED: Fan
            └─ NO → 팬 ON, 가습기 ON, RGB=Teal → LED: Fan,Humi

🚀 설치 및 실행
필수 사항

STM32CubeIDE 또는 Keil uVision
STM32 HAL 라이브러리
DHT11 라이브러리

설치 과정

저장소 복제git clone https://github.com/juntaek-oh/Smart-ENV_control-system.git
cd Smart-ENV_control-system


STM32CubeIDE에서 프로젝트 열기
핀 구성 확인 및 설정
빌드 및 업로드

⚙️ 설정
온도 임계값 설정
#define TEMP_HIGH_THRESHOLD   25    // 고온 기준 (25°C)
#define TEMP_MID_THRESHOLD    20    // 중간 온도 기준 (20°C)

습도 임계값 설정
#define HUMIDITY_HIGH         55    // 고습 기준 (55%)
#define HUMIDITY_MID          40    // 중간 습도 기준 (40%)

애니메이션 설정
#define ANIMATION_FRAME_DELAY 500  // 프레임 전환 주기 (ms)
#define ANIMATION_FRAMES      2    // 프레임 수

🔧 문제해결
일반적인 문제들

센서 읽기 오류: DHT11 연결 및 전원 공급 확인
RGB LED 색상 오류: PWM 설정 및 공통 캐소드 연결 확인
도트매트릭스 깜빡임: 시프트 레지스터 클록 신호 점검
LCD I2C 통신 오류: SCL/SDA 풀업 저항 확인

🤝 기여하기
이 프로젝트에 기여해주시는 모든 분들을 환영합니다!
📝 기여 방법

Fork the Project
Create Feature Branch (git checkout -b feature/AmazingFeature)
Commit Changes (git commit -m 'Add some AmazingFeature')
Push to Branch (git push origin feature/AmazingFeature)
Open Pull Request

🐛 버그 리포트
Issues 탭에서 다음 정보와 함께 버그를 리포트해 주세요:

하드웨어: STM32 보드 모델, 센서 모델 등
개발환경: STM32CubeIDE 버전, HAL 라이브러리 버전
에러 메시지: 컴파일 에러 또는 런타임 에러
재현 단계: 문제 발생 상황 및 절차
기대 동작: 예상했던 결과
실제 동작: 실제 발생한 결과

📞 연락처

이메일: ojt8416@gmail.com
GitHub Issues: 링크


  🌱 스마트 환경 제어로 쾌적한 실내 환경을 만들어보세요!
  STM32 임베디드 시스템과 다양한 센서의 융합으로 구현한 지능형 환경 제어
  7가지 RGB 상태 × 8가지 도트매트릭스 애니메이션 = 직관적 상태 표현
  ⭐ 도움이 되셨다면 Star를 눌러주세요! ⭐
  🔄 Pull Requests와 Issues를 환영합니다!
