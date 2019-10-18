# 2019-08-02 설치
### 1. 파이썬 홈페이지에서
### 2. 패키지 매니저 (Chocolatey, Homebrew 등)
- Chocolatey : package manager of window 

> ### choco install dockder-desktop
> ### choco install python 

### 3. pyenv

## 누산 Accumulate
### 누산기 Accumulator ex. 전자계산기

> ### age = 13
> ### age = 14 
: age 에 할당된 값을 갱신
> ### age = 13 + 1
> ### age = age + 1
: 요즘은 이렇게 짜지 말라고 함
> ### new_age = age + 1
> ### age = new_age

> ### age = age + 1
> ### age += 1

> ### age -= 1
> ### age *= 2
> ### age /= 2
> ### age //= 2
> ### age %= 2

## State Transition 상태변경

> ### factorial = 1
> ### factorial *= 1
> ### factorial *= 2
> ### factorial *= 3
> ### factorial *= 4
> ### factorial *= 5
> ### ...
> ### factorial *= n

> #### \# 초기값 
> ### factorial = 1
> #### \# 누산
> ### x는 1부터 n까지 > ### factorial *= x

- 코드로 작성
>### factorial = 1
>###
>### for x in range(1, n + 1):
>###    factorial *= x

# 2019-08-05

## 항등원 Identity Element
- 덧셈의 항등원 0
- 곱셈의 항등원 1

#### 예제 1) 점수의 총합, 평균
#### \# List 에서 바로 꺼내오기

total_score = 0
scores =[80, 100, 70, 90, 40]

for score in scores:
    total_score += score
    # print(total_score)

print(total_score)

#### \# range 사용

total_score = 0
scores =[80, 100, 70, 90, 40]

for i in range(len(scores)):
    total_score += scores[i]
    # print(total_score)

print(total_score)


#### 예제 3) 구구단
for n in range(2, 10):
    for i in range(1, 10):
        result = n * i
        print(n, '*', i, '=', result)

def multifly():
    for n in range(2, 10):
        for i in range(1, 10):
            result = n * i
            print(n, '*', i, '=', result)

#### \# 구구단 단별로 출력
def multifly(n):
    print(n, "단")
    for i in range(1, 10):
        result = n * i
        print(n, '*', i, '=', result)

multifly(8)

#### 예제 2) 여러명의 점수 총합, 평균
class_scores = [
    [30, 90, 80, 40, 50],
    [100, 100, 100, 100, 100],
    [90, 90, 30, 30, 20]
]

sum_scores = 0

for n in range(len(class_scores)):
    for i in class_scores[n]:
        sum_scores += i
        print(sum_scores)
print(sum_scores)

# 추상화 Abstraction
### : 구체적인 것을 구체적이지 않게 만드는 것
### : 공통적인 부분을 뽑아낸다

def function(parameter):
    return 1

print(function(argument))

# 2019-08-19
지난주 숙제 class_scores
