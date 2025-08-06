# SmartBarn-EnvControl
---

<div align="center">
  <img src="![시연영상](https://github.com/user-attachments/assets/656af57a-8e2c-44ed-969b-0d163622a047)
" width="320"/>
  <img src="![시연영상](https://github.com/user-attachments/assets/8d56b06a-245f-43cc-ad13-9cc70839f979)
" width="320"/>
</div>
<div align="center">
  <img src="![시연영상](https://github.com/user-attachments/assets/291d4899-3235-46b2-8313-0621d3945a85)
" width="320"/>
  <img src="![시연영상](https://github.com/user-attachments/assets/6024112f-56b1-487e-bd06-abed6e4dae64)
" width="320"/>
</div>

---

실내외 온·습도 실시간 모니터링, 자동 제어, 실시간 시각화를 모두 구현한 스마트 축사 환경 제어 시스템입니다.
STM32F411 MCU와 Raspberry Pi 4, 블루투스, MySQL, Grafana 등 다양한 하드웨어·소프트웨어 융합으로 축사 환경을 자동/직관적으로 관리합니다.

---

## 🔩 주요 기능 및 시스템 구조

- **실내·실외 온습도 동시 모니터링**
    - DHT11 센서 2개로 실내·실외 온·습도 측정
    - LCD 1602로 실시간 수치 표시

- **자동 환경 제어**
    - 내부 온도 기준 초과 시 선풍기(모터) 자동 ON/OFF
    - 내부 습도 기준 미달 시 가습기 모듈 자동 ON/OFF
    - RGB LED로 온도 구간별 상태 시각화(파랑/초록/빨강)
    - 8x8 도트매트릭스에 온도별 표정(스마일/슬픈 얼굴 등) 표시

- **블루투스 및 데이터 관리**
    - STM32→HC-06→Raspberry Pi 실시간 블루투스 데이터 전송
    - 수신 데이터 파싱 후 MySQL DB 저장(내외부 각각)
    - 그래프(Dashboard)는 Grafana에서 실시간으로 확인

---

## 🗂️ 하드웨어 및 부품

- **MCU:** STM32F411RE
- **센서:** DHT11 (2개, 실내·외)
- **표시 장치:** LCD1602, 8x8 Dot LED, RGB LED
- **제어 모듈:** EZ 모터 R300(선풍기), 가습기 모듈
- **통신:** HC-06 블루투스, Raspberry Pi 4
- **서버:** MySQL, Grafana

---

## ⚙️ 동작 흐름(Flow)

1. DHT11 센서 2개로 실내·외 온습도 주기적 측정
2. STM32에서 데이터 문자열 변환(IN:xx,yy OUT:aa,bb) 후 HC-06 블루투스 전송
3. Raspberry Pi에서 데이터 파싱 및 MySQL 저장
4. 내부 온도/습도 임계치 기반으로 선풍기·가습기 자동제어(ON/OFF)
5. LCD에는 온습도 수치, RGB LED/도트매트릭스에는 상태별 컬러·표정 표시
6. Grafana에서 DB 연동 온습도 변화 그래프 대시보드 제공

---

## 🛠️ 설치 및 실행법

1. **소스 다운로드 및 환경 설정**
    - STM32CubeIDE, Raspberry Pi, MySQL, Grafana 준비
2. **하드웨어 결선 및 펌웨어 업로드**
    - DHT11, LCD1602, Dot LED, 모터 등 핀 구성도에 맞게 연결
3. **블루투스/DB/Grafana 연동 후 운영**

---

## 🚩 주요 성과 및 특징

- 축사 환경 변화에 따른 자동 제어로 가축 폐사 방지, 생산성 향상
- 실시간 데이터 관리/시각화, 관리자 직관적 상태 확인
- 전압·타임아웃·에러 예외 상황 안정 처리

---

## 📷 예시 회로도 및 결과 사진/그래프

(프로젝트 진행 중 캡처, 결과 그래프, 회로 배선도 등 삽입)

---

## 🙋 문의/기여

사용/기여/협업 모두 환영합니다!

