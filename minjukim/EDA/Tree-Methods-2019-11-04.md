# Tree Methods 2019-11-04 선미님

Decision Tree

`Root Node` 뿌리 → `Intermediate Node` 가지 → `Leaf` /`Terminal Node` 잎

Label = Class = Dependent Variable = 종속변수

gini = impurirty 불순도 / entropy 

gini 가 낮아지는 방향으로 가지를 친다
→ 순도가 올라간다
→ 특정 라벨로 치우친다

gini 가 0.5 에 가까울수록 분류가 잘 안되는 상황

### Desicion Tree 종류

- Regressor
- Classifier

fitting 방식은 같다

마지막 leaf node 에서 어떤 값을 return 해주느냐

# Random Forest

하나의 모델이 잘못 만들어진 경우도 보정할 수 있다

Overfitting 방지

1. N 개의 데이터셋 만들기
2. N 개의 트리 만들기

n_estimators: tree 갯수

Emsemble 다양한 모델을 합친 것

앙상블을 하는 방식 중 하나 Bagging 방식

e.g. Decision Tree 를 Bagging 으로 Emsemble 해주면 Random Forest