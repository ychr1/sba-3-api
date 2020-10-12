"""1장 컴퓨터는 데이터에서 배운다
1.1 데이터를 지식으로 바꾸는 지능적인 시스템 구축
1.2 머신 러닝의 세 가지 종류
__1.2.1 지도 학습으로 미래 예측
__1.2.2 강화 학습으로 반응형 문제 해결
__1.2.3 비지도 학습으로 숨겨진 구조 발견
1.3 기본 용어와 표기법 소개
1.4 머신 러닝 시스템 구축 로드맵
__1.4.1 전처리: 데이터 형태 갖추기
__1.4.2 예측 모델 훈련과 선택
__1.4.3 모델을 평가하고 본 적 없는 샘플로 예측
1.5 머신 러닝을 위한 파이썬
__1.5.1 파이썬과 PIP에서 패키지 설치
__1.5.2 아나콘다 파이썬 배포판과 패키지 관리자 사용
__1.5.3 과학 컴퓨팅, 데이터 과학, 머신 러닝을 위한 패키지
1.6 요약

2장 간단한 분류 알고리즘 훈련
2.1 인공 뉴런: 초기 머신 러닝의 간단한 역사
__2.1.1 인공 뉴런의 수학적 정의
__2.1.2 퍼셉트론 학습 규칙
2.2 파이썬으로 퍼셉트론 학습 알고리즘 구현
__2.2.1 객체 지향 퍼셉트론 API
__2.2.2 붓꽃 데이터셋에서 퍼셉트론 훈련
2.3 적응형 선형 뉴런과 학습의 수렴
__2.3.1 경사 하강법으로 비용 함수 최소화
__2.3.2 파이썬으로 아달린 구현
__2.3.3 특성 스케일을 조정하여 경사 하강법 결과 향상
__2.3.4 대규모 머신 러닝과 확률적 경사 하강법
2.4 요약

3장 사이킷런을 타고 떠나는 머신 러닝 분류 모델 투어
3.1 분류 알고리즘 선택
3.2 사이킷런 첫걸음: 퍼셉트론 훈련
3.3 로지스틱 회귀를 사용한 클래스 확률 모델링
__3.3.1 로지스틱 회귀의 이해와 조건부 확률
__3.3.2 로지스틱 비용 함수의 가중치 학습
__3.3.3 아달린 구현을 로지스틱 회귀 알고리즘으로 변경
__3.3.4 사이킷런을 사용하여 로지스틱 회귀 모델 훈련
__3.3.5 규제를 사용하여 과대적합 피하기
3.4 서포트 벡터 머신을 사용한 최대 마진 분류
__3.4.1 최대 마진
__3.4.2 슬랙 변수를 사용하여 비선형 분류 문제 다루기
__3.4.3 사이킷런의 다른 구현
3.5 커널 SVM을 사용하여 비선형 문제 풀기
__3.5.1 선형적으로 구분되지 않는 데이터를 위한 커널 방법
__3.5.2 커널 기법을 사용하여 고차원 공간에서 분할 초평면 찾기
3.6 결정 트리 학습
__3.6.1 정보 이득 최대화: 자원을 최대로 활용
__3.6.2 결정 트리 만들기
__3.6.3 랜덤 포레스트로 여러 개의 결정 트리 연결
3.7 k-최근접 이웃: 게으른 학습 알고리즘
3.8 요약

4장 좋은 훈련 세트 만들기: 데이터 전처리
4.1 누락된 데이터 다루기
__4.1.1 테이블 형태 데이터에서 누락된 값 식별
__4.1.2 누락된 값이 있는 샘플이나 특성 제외
__4.1.3 누락된 값 대체
__4.1.4 사이킷런 추정기 API 익히기
4.2 범주형 데이터 다루기
__4.2.1 순서가 있는 특성과 순서가 없는 특성
__4.2.2 순서 특성 매핑
__4.2.3 클래스 레이블 인코딩
__4.2.4 순서가 없는 특성에 원-핫 인코딩 적용
4.3 데이터셋을 훈련 세트와 테스트 세트로 나누기
4.4 특성 스케일 맞추기
4.5 유용한 특성 선택
__4.5.1 모델 복잡도 제한을 위한 L1 규제와 L 2 규제
__4.5.2 L 2 규제의 기하학적 해석
__4.5.3 L1 규제를 사용한 희소성
__4.5.4 순차 특성 선택 알고리즘
4.6 랜덤 포레스트의 특성 중요도 사용
4.7 요약

5장 차원 축소를 사용한 데이터 압축
5.1 주성분 분석을 통한 비지도 차원 축소
__5.1.1 주성분 분석의 주요 단계
__5.1.2 주성분 추출 단계
__5.1.3 총분산과 설명된 분산
__5.1.4 특성 변환
__5.1.5 사이킷런의 주성분 분석
5.2 선형 판별 분석을 통한 지도 방식의 데이터 압축
__5.2.1 주성분 분석 vs 선형 판별 분석
__5.2.2 선형 판별 분석의 내부 동작 방식
__5.2.3 산포 행렬 계산
__5.2.4 새로운 특성 부분 공간을 위해 선형 판별 벡터 선택
__5.2.5 새로운 특성 공간으로 샘플 투영
__5.2.6 사이킷런의 LDA
5.3 커널 PCA를 사용하여 비선형 매핑
__5.3.1 커널 함수와 커널 트릭
__5.3.2 파이썬으로 커널 PCA 구현
__5.3.3 새로운 데이터 포인트 투영
__5.3.4 사이킷런의 커널 PCA
5.4 요약

6장 모델 평가와 하이퍼파라미터 튜닝의 모범 사례
6.1 파이프라인을 사용한 효율적인 워크플로
__6.1.1 위스콘신 유방암 데이터셋
__6.1.2 파이프라인으로 변환기와 추정기 연결
6.2 k-겹 교차 검증을 사용한 모델 성능 평가
__6.2.1 홀드아웃 방법
__6.2.2 k-겹 교차 검증
6.3 학습 곡선과 검증 곡선을 사용한 알고리즘 디버깅
__6.3.1 학습 곡선으로 편향과 분산 문제 분석
__6.3.2 검증 곡선으로 과대적합과 과소적합 조사
6.4 그리드 서치를 사용한 머신 러닝 모델 세부 튜닝
__6.4.1 그리드 서치를 사용한 하이퍼파라미터 튜닝
__6.4.2 중첩 교차 검증을 사용한 알고리즘 선택
6.5 여러 가지 성능 평가 지표
__6.5.1 오차 행렬
__6.5.2 분류 모델의 정밀도와 재현율 최적화
__6.5.3 ROC 곡선 그리기
__6.5.4 다중 분류의 성능 지표
6.6 불균형한 클래스 다루기
6.7 요약

7장 다양한 모델을 결합한 앙상블 학습
7.1 앙상블 학습
7.2 다수결 투표를 사용한 분류 앙상블
__7.2.1 간단한 다수결 투표 분류기 구현
__7.2.2 다수결 투표 방식을 사용하여 예측 만들기
__7.2.3 앙상블 분류기의 평가와 튜닝
7.3 배깅: 부트스트랩 샘플링을 통한 분류 앙상블
__7.3.1 배깅 알고리즘의 작동 방식
__7.3.2 배깅으로 Wine 데이터셋의 샘플 분류
7.4 약한 학습기를 이용한 에이다부스트
__7.4.1 부스팅 작동 원리
__7.4.2 사이킷런에서 에이다부스트 사용
7.5 요약

8장 감성 분석에 머신 러닝 적용
8.1 텍스트 처리용 IMDb 영화 리뷰 데이터 준비
__8.1.1 영화 리뷰 데이터셋 구하기
__8.1.2 영화 리뷰 데이터셋을 더 간편한 형태로 전처리
8.2 BoW 모델 소개
__8.2.1 단어를 특성 벡터로 변환
__8.2.2 tf-idf를 사용하여 단어 적합성 평가
__8.2.3 텍스트 데이터 정제
__8.2.4 문서를 토큰으로 나누기
8.3 문서 분류를 위한 로지스틱 회귀 모델 훈련
8.4 대용량 데이터 처리: 온라인 알고리즘과 외부 메모리 학습
8.5 잠재 디리클레 할당을 사용한 토픽 모델링
__8.5.1 LDA를 사용한 텍스트 문서 분해
__8.5.2 사이킷런의 LDA
8.6 요약

9장 웹 애플리케이션에 머신 러닝 모델 내장
9.1 학습된 사이킷런 추정기 저장
9.2 데이터를 저장하기 위해 SQLite 데이터베이스 설정
9.3 플라스크 웹 애플리케이션 개발
__9.3.1 첫 번째 플라스크 애플리케이션
__9.3.2 폼 검증과 화면 출력
9.4 영화 리뷰 분류기를 웹 애플리케이션으로 만들기
__9.4.1 파일과 폴더: 디렉터리 구조 살펴보기
__9.4.2 메인 애플리케이션 app.py 구현
__9.4.3 리뷰 폼 구성
__9.4.4 결과 페이지 템플릿 만들기
9.5 공개 서버에 웹 애플리케이션 배포
__9.5.1 PythonAnywhere 계정 만들기
__9.5.2 영화 분류 애플리케이션 업로드
__9.5.3 영화 분류기 업데이트
9.6 요약

10장 회귀 분석으로 연속적 타깃 변수 예측
10.1 선형 회귀
__10.1.1 단변량 선형 회귀
__10.1.2 다변량 선형 회귀
10.2 주택 데이터셋 탐색
__10.2.1 데이터프레임으로 주택 데이터셋 읽기
__10.2.2 데이터셋의 중요 특징 시각화
__10.2.3 상관관계 행렬을 사용한 분석
10.3 최소 제곱 선형 회귀 모델 구현
__10.3.1 경사 하강법으로 회귀 모델의 파라미터 구하기
__10.3.2 사이킷런으로 회귀 모델의 가중치 추정
10.4 RANSAC을 사용하여 안정된 회귀 모델 훈련
10.5 선형 회귀 모델의 성능 평가
10.6 회귀에 규제 적용
10.7 선형 회귀 모델을 다항 회귀로 변환
__10.7.1 사이킷런을 사용하여 다항식 항 추가
__10.7.2 주택 데이터셋을 사용한 비선형 관계 모델링
10.8 랜덤 포레스트를 사용하여 비선형 관계 다루기
__10.8.1 결정 트리 회귀
__10.8.2 랜덤 포레스트 회귀
10.9 요약

11장 레이블되지 않은 데이터 다루기: 군집 분석
11.1 k-평균 알고리즘을 사용하여 유사한 객체 그룹핑
__11.1.1 사이킷런을 사용한 k-평균 군집
__11.1.2 k-평균 ++로 초기 클러스터 센트로이드를 똑똑하게 할당
__11.1.3 직접 군집 vs 간접 군집
__11.1.4 엘보우 방법을 사용하여 최적의 클러스터 개수 찾기
__11.1.5 실루엣 그래프로 군집 품질을 정량화
11.2 계층적인 트리로 클러스터 조직화
__11.2.1 상향식으로 클러스터 묶기
__11.2.2 거리 행렬에서 계층 군집 수행
__11.2.3 히트맵에 덴드로그램 연결
__11.2.4 사이킷런에서 병합 군집 적용
11.3 DBSCAN을 사용하여 밀집도가 높은 지역 찾기
11.4 요약

12장 다층 인공 신경망을 밑바닥부터 구현
12.1 인공 신경망으로 복잡한 함수 모델링
__12.1.1 단일층 신경망 요약
__12.1.2 다층 신경망 구조
__12.1.3 정방향 계산으로 신경망 활성화 출력 계산
12.2 손글씨 숫자 분류
__12.2.1 MNIST 데이터셋 구하기
__12.2.2 다층 퍼셉트론 구현
12.3 인공 신경망 훈련
__12.3.1 로지스틱 비용 함수 계산
__12.3.2 역전파 알고리즘 이해
__12.3.3 역전파 알고리즘으로 신경망 훈련
12.4 신경망의 수렴
12.5 신경망 구현에 관한 몇 가지 첨언
12.6 요약

13장 텐서플로를 사용하여 신경망 훈련
13.1 고성능 머신 러닝 라이브러리 텐서플로
__13.1.1 텐서플로란?
__13.1.2 텐서플로 학습 방법
__13.1.3 텐서플로 시작
__13.1.4 배열 구조 다루기
__13.1.5 텐서플로 저수준 API로 간단한 모델 개발
13.2 tf.keras API로 다층 신경망 훈련
__13.2.1 훈련 데이터 준비
__13.2.2 피드포워드 신경망 구성
__13.2.3 피드포워드 신경망 훈련
13.3 다층 신경망의 활성화 함수 선택
__13.3.1 로지스틱 함수 요약
__13.3.2 소프트맥스 함수를 사용하여 다중 클래스 확률 예측
__13.3.3 하이퍼볼릭 탄젠트로 출력 범위 넓히기
__13.3.4 렐루 활성화 함수
13.4 요약

14장 텐서플로의 구조 자세히 알아보기
14.1 텐서플로의 주요 특징
14.2 텐서플로의 랭크와 텐서
__14.2.1 텐서의 랭크와 크기를 확인하는 방법
14.3 텐서를 다차원 배열로 변환
14.4 텐서플로의 계산 그래프 이해
14.5 텐서플로의 변수
14.6 tf.keras API 자세히 배우기
__14.6.1 Sequential 모델
__14.6.2 함수형 API
__14.6.3 tf.keras 모델의 저장과 복원
14.7 계산 그래프 시각화
__14.7.1 텐서보드 익숙하게 다루기
__14.7.2 케라스의 층 그래프 그리기
14.8 요약

15장 심층 합성곱 신경망으로 이미지 분류
15.1 합성곱 신경망의 구성 요소
__15.1.1 CNN과 특성 계층 학습
__15.1.2 이산 합성곱 수행
__15.1.3 서브샘플링
15.2 기본 구성 요소를 사용하여 심층 합성곱 신경망 구성
__15.2.1 여러 개의 입력 또는 컬러 채널 다루기
__15.2.2 드롭아웃으로 신경망 규제
15.3 텐서플로를 사용하여 심층 합성곱 신경망 구현
__15.3.1 다층 CNN 구조
__15.3.2 데이터 적재와 전처리
__15.3.3 텐서플로 tf.keras API로 CNN 구성
__15.3.4 합성곱 신경망 모델 훈련
__15.3.5 활성화 출력과 필터 시각화
15.4 요약

16장 순환 신경망으로 시퀀스 데이터 모델링
16.1 시퀀스 데이터 소개
__16.1.1 시퀀스 데이터 모델링: 순서를 고려한다
__16.1.2 시퀀스 표현
__16.1.3 시퀀스 모델링의 종류
16.2 시퀀스 모델링을 위한 RNN
__16.2.1 RNN 구조와 데이터 흐름 이해
__16.2.2 RNN의 활성화 출력 계산
__16.2.3 긴 시퀀스 학습의 어려움
__16.2.4 LSTM 유닛
16.3 텐서플로의 tf.keras API로 시퀀스 모델링을 위한 다층 RNN 구현
16.4 첫 번째 프로젝트: 다층 RNN으로 IMDb 영화 리뷰의 감성 분석 수행
__16.4.1 데이터 준비
__16.4.2 임베딩
__16.4.3 RNN 모델 만들기
__16.4.4 감성 분석 RNN 모델 훈련
__16.4.5 감성 분석 RNN 모델 평가
16.5 두 번째 프로젝트: 텐서플로로 글자 단위 언어 모델 구현
__16.5.1 데이터 전처리
__16.5.2 글자 단위 RNN 모델 만들기
__16.5.3 글자 단위 RNN 모델 훈련
__16.5.4 글자 단위 RNN 모델로 텍스트 생성
16.6 전체 요약"""