### 기초 설명

한국의 약 2,000개 상점의 신용카드 거래 내역이 제공됩니다. card_id를 기준으로 샘플링되었으며, amount의 단위는 KRW가 아닙니다. 테스트 파일에서 각 상점의 마지막 매출 발생일 다음 날부터 100일 후까지 매출의 총합을 예측해야 합니다.

예측한 금액만큼 100일간 대출을 진행합니다. 만약 예측한 금액보다 실제 매출이 적게 발생한다면 원금에 손실을 보게 됩니다. 실제 매출이 예측한 금액 이상으로 발생한다면, 연이율 13%의 이자가 발생합니다.

### 거래 지표 요소
상점 고유 번호, 거래일자, 거래시간, 카드번호, 매출 금액, 할부 개월 수, 요일, 공휴일

### 생각해볼 수 있는점

1. 월별에 따른 매출 변동
2. 거래 시간에 따른 매출 변동
3. 요일에 따른 매출 변동
4. 주중 대비 휴일 매출 변동
5. 평균 할부 금액 대비 타 매출의 평균 매출 변동
6. 거래 횟수에 따른 매출 변동
7. 카드 번호별 결재 금액
8. 전일 대비 매출 변화량
9. 전 거래 대비 매출 변화량
10. (추가중)