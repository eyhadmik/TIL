# SQL/PANDAS_12

### 데모데이 팁

- 선미님 퍼블릭 스피킹 팁: 시간엄수. 웃긴거, 나누고 싶은 엑기스만 발표. 코드는 슬랙에 공유하여라

## 우리는 지금까지

데이터 분석을 하기 위해 필요한 기초적인 기술 교육, 스스로 학습해 나갈 수 있는 자세 만들기에 집중했습니다. 3개월 반 교육과정 동안 스스로 학습하는 자세가 바뀌었다고 느끼시나요? 저는 첫 날 아무것도 모르던 여러분들이 파이썬 코드를 줄줄 짜고, 데이터 분석 용어로 농담하는 걸 보는게 신기해요.

- 데이터 분석가에게 필요한 Python 기초
- Git, Github 사용 기초
- 통계
- Pandas, statsmodel, sklearn, matplotlib 등 데이터 분석하는데 필요한 파이썬 패키지
- Intermediate SQL
- 웹 크롤링, 추천시스템 등 스페셜 토픽 소개 및 실습
- 프로젝트를 통한 데이터 분석 멘토링
- 네트워킹, Public speaking 경험 쌓기

## 앞으로는

필수 기술 교육은 지난 3개월 반 동안 충분히 했습니다! 지금부터는 머신러닝 기초, 자연어처리 등 세부 토픽들을 다룹니다. 지난 교육기간 동안 배웠던 내용들을 정리합니다. 프로젝트를 통해 기술 숙련도를 높이고, 데이터 읽는 법을 훈련합니다.

- 통계 Wrap up, 통계 활용의 팁
- SQL Subqueries, Aggregate functions
- 자연어처리
- 머신러닝 기초 (트리계열 알고리즘, 데이터 전처리, 모델 평가 등)
- 데모데이 프로젝트 멘토링

## 이런 것들을 여러분께 기대해요

- 여러분들의 포트폴리오가 될, 데모데이 프로젝트에 적극적으로 참여해주셨으면 좋겠어요. 데모데이 뿐만 아니라 내년 데이터야놀자, DSTS, 파이콘, 파이콘 격월 세미나 등 다양한 곳에서 우리의 경험과 성과를 떠들어주셨으면 합니다.
- 지난 수업들을 차근차근 복습해주세요. 새로운 노트북 또는 텍스트 파일을 열고 지난 코드들을 완전히 새로 생각해 작성하는 경험을 해보셨으면 좋겠어요. 그 과정에서 더 좋은 코드와 아이디어를 발견하게 되실거예요. 복습 과정에서 수업 자료에 업데이트가 필요한 부분을 발견하셨다면 Teaching-Materials, homework 레포에 PR 주세요. 생각만큼 빨리빨리 안되어서 괴로운 분들도 있을겁니다. 원래 새롭게 배운 지식을 유창하게 숙련자처럼 쓰기까지는 오랜 시간이 걸립니다. 옆에 있는 사람들이 나보다 잘 한다면, 코드를 한 줄 더 쳐보고 한 번 더 고민을 해봤기 때문이지 다른 이유는 없습니다.
- 데잇걸즈 프로그램이 앞으로 한 달 남았습니다. 데이터 분석 부트캠프 역사상 아마도 유례가 없을 길고 긴 프로젝트가 끝나가는데요. 밀도높은 공부를 오래간 하느라 고생 많으셨어요. 스스로의 성과를 칭찬해주세요.

- **선미선생님의 망코드를 향한 조언**
    - 여러분을 지울 수 없듯이 코드도 지울 수 없어요
    - 못난 코드도 잘 고쳐서 쓰세요

# Tree methods

- classification 문제를 유난히 잘 풀 수 있는 tree methods

## Decision Tress

- 면접 가서 가지 라고 하지 말고 intermediate node라고 말하기 ^^
- 잎 → 결과라고 생각하면 됨

![](Untitled-5a6ffad2-6e0c-47fd-a8e2-c201ac616170.png)

- 루트 노드의 클래스는 suvived(라벨, 타겟 벨류, 클래스, 와이, 디펜던트 variable,종속변수 등등,,,)고 samples는 891, value는 살아있는 사람/죽은 사람 이라는 라벨

![](Untitled-fd3cab34-b7e4-45b8-a239-5686750249e1.png)

- 어떤 기준으로 가지치기 했는 지 (sex가 0.5보다 작은 거 true/flase)
- ginig - 불순도 (entropy) : 지니가 낮아지는 방향으로 가지를 침
- 그래서 루트 노드의 지니는 0.473인데 인터미디어트 노드 지니는 더 낮음
- 불순도가 낮아진다? → 순도가 올라간다 : 박스에 들어있는 value가 한 쪽으로 치우친다 = 특정 라벨로 몰린다
- 그럼 맨 마지막 왼쪽의 애는 순도가 제일 높으니까, 살아남은 사람들의 모임이라고 할 수 있고 오른쪽은 젤 순도가 낮으니까 죽은 사람이라고 할 수 있음. 이렇게 분류하게 만들어지는 구조
- 근데 사실 이 박스는 의미가 없는 게, 마지막 잎 노드가 필요없음. 어차피 두번째에서 살고 죽음이 나옴. (여자면 살림) 그니까 마지막 분류 요금이 그닥 중요하지 않다고 생각할 수 있음. (fare)

![](Untitled-cea8a3f9-67f2-4450-98db-e64ffac2aec2.png)

![](Untitled-89147fda-c718-4ea1-9d6b-dc406823de0d.png)

- 이렇게 아래쪽으로 내려오면서 분류되는 정보를 인포메이션 gain(정보 획득)이라고도 함

### sklearn code

- randome_state를 42로 잡고 - 의사결정나무가 랜덤한 성격을 가지고 있음/ 설정을 안해주면 돌릴 때마다 예측이 달라짐. 그래서 정해주는 거. 42라는 숫자를 좋아해서 잡은 거임. thanks for my random_state라고 하기도 함.
- max_depth=2 (가지를 두번침) 안하면 많이 쳐지기도 함. 그럼 overfitting 나올 수도 있음.
- max_leaf_nodes=4 (잎 4개) 안하면 위랑 똑같. 최적의 숫자를 내가 찾아야함 (depth, nodes 등 하이퍼파라미터들)
- 하이퍼파라미터 = 머신러닝이 정하지 못하고 인간이 정해야하는 기준

![](Untitled-af534ff0-48f7-4746-84c7-ad3ba195ab12.png)

## Impurity

- 의사결정나무가 가장 낮춰야한다고 생각하는 팩터
- 의사결정나무는 Impurity (불순도, 불확실성)이 낮아지는 방법으로 학습합니다.
- 순도가 증가하는 것을 두고 Information gain이라고 하기도 합니다.
- 오늘은 의사결정나무의 불순도 측정 방법 중, Gini Index를 공부합니다.

- 지니 계산
- p = 0.5 (데이터가 5:5로 딱 들어가 있을 때) - 산 사람 500명, 죽은 사람 500명 ⇒ 트리에서 맨 위에있는 root node가 불순도가 가장 높을 거임. 그걸 낮춰가는 모델을 만드는 거니까
- 예를 들면 p는 891/549 임 (samples/value의 값)
- [https://imgur.com/n3MVwHW](https://imgur.com/n3MVwHW)

![](Untitled-811cad0a-007c-4856-a91d-2b91385c4070.png)

- 불순도의 최고치는 0.5다 (클래스가 두 개일때) / 세 개면 0.73 일 듯
- 왜냐? 10개의 데이터 일 때 5개, 5개로 나누어진다면
- 0.5^2 + 0.5^2 = 0.5 여기서 1-0.5 하면 결국 0.5임.
- step 1. 지니 계산
    - (549/891)^2 + (342/891)^2 = 0.5269
    - 1 - 0.5269 = 0.473
- step 2. 지니 계산
    - (361/415)^2 +(54/415)^2 =
    - 1 - 0.774= 0.226

![](Untitled-aae9f827-62af-4ee4-bc7f-c209a8ef5794.png)

## Random Forest

- 여러 트리들을 '다르게' 만든다
- [https://www.researchgate.net/figure/Architecture-of-the-random-forest-model_fig1_301638643](https://www.researchgate.net/figure/Architecture-of-the-random-forest-model_fig1_301638643)

![](Untitled-efc56b9e-c4fd-4e4c-99d8-2a01f506d6fa.png)

![](Untitled-db269abd-43b8-4ef6-98bb-e0cb4cdcce02.png)

- [https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/Seeing-the-Forest-for-the-Trees-An-Introduction-to-Random-Forest/ta-p/158062](https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/Seeing-the-Forest-for-the-Trees-An-Introduction-to-Random-Forest/ta-p/158062)

### Bagging

- 배깅(bagging)은 bootstrap aggregating의 약자로, 부트스트랩(bootstrap)을 통해 조금씩 다른 훈련
데이터에 대해 훈련된 기초 분류기(base learner)들을 결합(aggregating)시키는 방법이다.
- 부트스트랩이란, 주어진 훈련 데이터에서 중복을 허용하여 원 데이터셋과 같은 크기의 데이터셋을 만드는
과정을 말한다. 배깅을 통해 랜덤 포레스트를 훈련시키는 과정은 다음과 같이 세 단계로 진행된다.
1. 부트스트랩 방법을 통해 N개의 훈련 데이터셋을 생성한다.
2. N개의 기초 분류기(트리)들을 훈련시킨다.
3. 기초 분류기(트리)들을 하나의 분류기(랜덤 포레스트)로 결합한다(평균 또는 과반수투표 방식 이용).

![](Untitled-8656051c-2c49-4885-a2f5-3b9e0973c839.png)

![](Untitled-f7a04da3-ca1d-4564-8c39-d7c31ab232e5.png)

- 보통 하이퍼파라미터 1000개면 많은 거(우리가 돌리는 데이터에서) - 우리가 직접 시간을 들여서 찾아야 함

### bagging 일반화

- 트리를 bagging 방식으로 만든 게 random forest
- 앙상블 : 다양한 모델 결과를 합치는 것