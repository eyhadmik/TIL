# 추천 시스템2

### Bonus[예측 평점을 아래처럼 바꿔 계산하는 것이 기존 모델과 어떤 부분에서 다른지 생각해보기]

- 왜 다를까?
- 처음 만든 수식은 내가 보지 않은 영화에 대해서는 평점을 내릴 수 없는데,
- 두번째로 바꾼 수식은 내가 보지 않은 영화는 나의 평균 평점으로 점수를 측정해줌
- 평균에서부터 얼마나 벗어났는 지를 반영함
- 유저마다의 평균은 다 다르지만 비슷한 유저들은 평균들의 레인지는 비슷할거야(실제 평균값은 다르더라도! - 왜냐면 나는 평균이 8 점인데 우주님은 5점일수도 있지만, 주는 range는 비슷하다는 말)

    라는 가설에서 시작 

- 라이브러리 기능을 구현하는 함수를 짜는 게 코딩테스트로 나옴 (흑흑)

# 영화 추천 시스템 만들기

### 새로운 모델

- 지금까지 우리는 기본적인 모델들을 봤다 (저번 필기 참고)
- 문제는 아이템의 수가 늘어감에 따라 걸리는 시간이 기하급수적으로 늘어남 - 비효율적

**Latent Factor Model** 

- 어디서 추천 시스템 좀 공부해봤다 ~~~ 하는 모델
- 소비자, 아이템에 각각 잠재적인 특성(latent factor)이
있다고 가정하고 이를 학습하고자 하는 모델
    - 유저가 아이템을 소비한 기록만 가지고 잠재적인 축을 만들어서 컨텐츠를 읽지 않고도 추천해주는 모델
    - Latent factor는 주로 𝑛차원 벡터로 표현
        - 유저 1이 로맨스를 좋아한다면 로맨스 위주로 추천해준다
        - 어떻게 학습하나요?  → Matrix Factorization (MF)

### Matrix Factorization (MF)

- 소비자의 영화에 대한 평점 데이터는 행렬로 표현할 수 있음
- 표현한 행렬을 서로 다른 두 저차원 행렬의 곱으로 나타낼 수 있도록 (복원할 수 있도록) 저차원 행렬을 학습하는 방법
- 유저가 아이템을 소비한 이력, 혹은 평점 정보 (한 축은 유저, 한 축은 소비 이력 또는 평점) 을 행렬 화 → 저차원 행렬로 분열 (4x4 행렬을 복원할 수 있는 2x2 , 2x2로 바꿈)

![](Untitled-4d25067b-f701-4f26-b3d9-7c7473d7860d.png)

- 로맨스 영화를 좋아하고, 액션 영화를 싫어하는 소비자의 latent factor (user factor / user feature)
    - 𝑝𝑢 = (1.9, −2.4)
- 로맨스 영화의 latent factor (item factor / item feature)
    - 𝑞𝑖 = (2.7, −1.9)
- 두 latent factor로 부터 계산한 예측 평점
    - 1.9, → 벡터 좌표를 쓸 때 표현하는 거 (뒤에 콤마)
    - 결론 = 유저 u의 선호 특성 / i 라는 영화의 특성 을 내적함 —> 9.69

![](Untitled-ce3e3a3b-abfb-40de-80bc-2158705f7f6b.png)

### 장점

- Matrix Factorization의 장점
    - User / Item을 표현하는 **저차원(low dimensional) 밀집 벡터(dense vector)**를 얻을 수 있어서 다양한 머신러닝 / 데이터 분석 방법을 적용할 수 있음

        • Cluster analysis, 다른 모델의 입력으로 사용

        ![](Untitled-0e866b31-826e-4b58-919d-2d495500d0fe.png)

    - 복원하고자 하는 행렬을 어떻게 구성하냐에 따라 다양하게 활용할 수 있음
        - 다양한 워드 임베딩 모델 중 일부는 단어-단어 행렬을 구성하고 matrix factorization을 적용한 것
            - Word2Vec(Mikolovet.al,2013)–SPPMI
            - GloVe(Penningtonet.al,2014)–Co-occurrenceprob.
            - 예를 들면 아이스크림, 얼음은 같이 자주 등장하는 단어 셋이다 → 행렬화 시켜서 학습 시킴
        - 소셜 네트워크 데이터를 활용해 사용자-사용자 행렬을 구성하고 matrix factorization을 적용해 사용자 특성 추출
            - 트위터나 페이스북에서 유저 - 유저 친구관계를 긁어라
        - 데이터가 많아지면 고차원의 모델들을 적용하는 데 힘들다. 그렇지만 mf는 데이터셋에 유연하게 접근이 잘 되고, 간단하게 할 수 있어서 인기가 좋음 (저 차원의 dense bector)

### 수식

- 앞에 배웠던 모델과 지금 모델의 차이?
- 지금 모델이 저차원 벡터를 잘 학습시키도록 함 (차원 값이 작아져도 잘 학습됨)
- 기본모형

![](Untitled-a3579c60-e226-475a-bd56-af3a5a97bdb0.png)

- 벡터의 모든 값들의 제곱의 합 (+ 뒤의 수식) → 저차원 벡터를 잘 학습 시키도록 - 너무 값이 커져서 복잡해지지 않게 (pu랑 qi가 차원이 만개씩 되면 너무 커지는 데 우리가 원하는 건 그냥 적당한 크기)

![](Untitled-dde136c8-5bb3-4c07-9614-25e0df712520.png)

![](Untitled-5396e018-59c1-495b-8105-14a8dca79273.png)

### 구현하기

1. 지난번에 구현했던 User-User CF를 Surprise 라이브러리로 수행해보기 (같이)

2. [Matrixfactorization을 Surprise 라이브러리로 수행해보기 (SVD)](https://surprise.readthedocs.io/en/stable/matrix_factorization.html#surprise.prediction_algorithms.matrix_factorization.SVD)

- 파라미터 설명
    - n_factors – 올라갈 수록 모델이 복잡해짐 (모델 학습 팩터) / 어느 수준까지는 오를 수록 똑똑해짐/ 올라갈 수록 epoch 수도 올리는 게 좋다 : 한 행렬의  개수
    - (예를 들면 여기서 n_factors = 200개이면,  w가 200개의 열)

    ![](Untitled-4d25067b-f701-4f26-b3d9-7c7473d7860d.png)

    - n_epochs – 전체 데이터 학습 시키는 횟수
    - biased (bool) – 바이어스드. r을 p와 q의 곱으로 설명하겠다.
    - lr_all – 러닝 레이트. 모든 파라미터에 대해서 똑같은 running late를 적용한다. 로스에서 가장 작은 값을 찾을 때 lr이 크면 많이 가고, 작으면 적게 간다. 그래서 lr이 크면 epoch도 많아야 좋음
    - reg_all – p랑 q에 regularlize를 얼마나 할거냐, 많이 하면 바보가 됨 (커지면 커질 수록 람다 뒤의 값이 작아져서 설명력을 잃게 됨)
    - reg_bu – b가 뭘까? svd 설명을 보면 최소화하는 대상이 적혀있음. 유저의 평점 bias를 학습시키는 모델.
    - random_state
    - verbose – 현재 어디까지 되고 있는 지 알려주는 수다스러운 옵션 (어디까지 했는 지 내가 주기적으로 알려줄게)

3. Matrix factorization의 다양한 옵션을 문서에서 확인해보고 바꿔서 결과 확인해보기

### Funk’s SVD

- 소비자의 기본 성격과 아이템의 기본 인기도를 bias로 표현하여 모델에 반영
- 2006년 넷플릭스 프라이즈 우승 모델
- Surprise SVD에서 biased=True (기본값) 옵션을 주면 Funk’s SVD를 사용함
- 바이어스? 전체에 대한 유저들의 평점과 아이템에 대한 평균을 알 수 있게 해줌. (대부분 평균값이랑 가까워짐) 그래서 더 학습 된 머신러닝이라고 할 수 있음

![](Untitled-43efa6f3-541b-483f-a029-e997b4a5daae.png)

### 유사 엔티티 분석

- p와 q 행렬(매트릭스)가 생기면 그 안에서 값을 꺼내서 비슷한 유저나 item을 찾을 수 있음
- MF를 통해 얻은 latent factor로 유사한 소비자나 아이템을 찾아 분석하는 것이 가능
- 일반적으로 matrix factorization으로 학습한 latent factor는 cosine similarity로 유사도를 측정

![](Untitled-c098321a-51e3-408a-8492-4ad6d068a612.png)

- Surprise 라이브러리의 matrix factorization 모델은 latent factor를 변수에 저장해 줌
    - pu = user latent factor
    - qi = item latent factor
- DataFrame에 들어있던 userid / itemid를 matrix row, column index로 변환해서 접근해야 함

### 시각화 툴을 이용한 유사 엔티티 분석

- Tensorflow Embedding Projector
- 자동으로 해주는 툴 이미 있음 : tensorflow embedding projector
- [위키피디아 로](https://projector.tensorflow.org) 만든 예제
    - qi.tsv: 한 줄에 qi 벡터가 하나씩 출력되어야 함 (tab separated)
    - titles.tsv : 한줄에 영화 제목이 하나씩 출력되어야 함
- 데이터를 업로드해 여러가지 영화의 유사영화를 확인해보며 분석을 해보기
    - 파일 2개 생성하기 (load) 클릭
    - 1. model.qi를 데이터 프레임으로 바꾼 후, tsv 파일로 저장해서 로드하기

    ![](Untitled-143e63d6-8b11-4062-ad2c-a7819bccf361.png)

    - 2. model.qi 파일 + 메타데이터 파일(이게 있어야 영화 정보를 바로 알 수 있음)

    ![](Untitled-e1bb1b5f-4630-4949-9b38-990b4399adb9.png)