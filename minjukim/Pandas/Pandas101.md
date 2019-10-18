# Pandas
- R 베이스의 언어
    - R 은 통계 특화 언어
- Python 과는 문법이 다르다
- 사용자도 많고 기능이 많은 라이브러리

Python | Pandas
------|------
List | Series
Table | DataFrame

null 값 (np.nan) 이 하나 들어가면 해당 컬럼은 다 실수형이 된다

df.sort_index(axis=0, ascending=True)
- axis = 0, index 로 sort
- axis = 1, column 으로 sort
- ascending : 거꾸로 정렬

> df.sort_values(by='E', ascending=True)
: 특정 column 의 값으로 sorting

>### dataframe.loc[index, column]
>### df.loc[2, :]
: 전체
![df.loc[2, :] 캡쳐화면]()

![df.loc[2:3, ['A', 'C']] 캡쳐화면]()

> df.describe()
![tips.describe() 캡쳐화면]()
std: 표준편차

> tips['smoker'].unique()

SQL 의 DISTINCT

> tips[tips['smoker'] == 'Yes'].head(3)

SQL 의 WHERE

## 요일별 팁을 준 손님 수
> tips.groupby('day').size()

> tips["day"].value_counts()