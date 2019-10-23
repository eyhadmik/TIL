# PYTHON3-15

# 파이썬 코딩 문제 풀이

“모의고사” 문제

[https://programmers.co.kr/learn/courses/30/lessons/42840](https://programmers.co.kr/learn/courses/30/lessons/42840)

아샬의 풀이

[https://github.com/ahastudio/CodingLife/blob/master/20191022/python/test_example.py](https://github.com/ahastudio/CodingLife/blob/master/20191022/python/test_example.py)

## How to Solve It

1. 문제 이해
2. 계획 수립
3. 계획 실행
4. 반성

각 단계는 순서가 있지만, 필요에 따라 이전 단계로 돌아갈 수 있습니다. 피드백을 통해 빠르게 반복하는 사이클을 만들면 좋습니다.

오스틴의 나비

[https://youtu.be/hqh1MRWZjms](https://youtu.be/hqh1MRWZjms)

각 단계의 수행을 돕는 템플릿

[https://howtosolveit.herokuapp.com/](https://howtosolveit.herokuapp.com/)

## 무엇을 알아내야 하나?

- 가장 많이 맞춘 학생
    - 단수? 복수? → 복수
        - 순서는 어떻게 되나?
    - 각 학생의 점수를 어떻게 알 수 있나?
        - 어떻게 채점하지?
        - 채점 결과를 어떻게 관리하지?
    - 가장 점수가 높은 학생을 어떻게 찾을 수 있나?
        - 가장 높은 점수는 몇 점인가?
        - 가장 높은 점수를 이용해 학생 목록을 얻을 수 있을까?
    - 각 학생이 어떻게 답할지 알 수 있을까?
        - 각 학생의 찍기 패턴은 어떻게 되나?
        - 패턴을 어떻게 반복시킬까?

## 테스트 코드 작성

1. 문제 전체에 대한 조망
    - Top Down으로 한번 살펴보기
    - 각 부분이 완결되고 조립되면 자연스럽게 통과
2. N번 문제에 대한 학생의 답 알아내기
3. N번 문제를 맞췄는지 검사하기
4. 몇 개의 문제를 맞췄는지 계산하기
5. 점수가 가장 높은 학생 알아내기

### 내 풀이

- 어렵지만 코드 하나하나 살펴보면서 거의 개인 과외 식으로...이해함

    MAX_PROBLEMS = 10_000
    
    PATTERNS = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5], # 컴마가 있어도 돌아감, 실수를 방지하기 위해
    ]
    
    def good_students(answers):
        # 점수 계산
        scores = []
    
        # 1. 답
        students_answers = [1, 2, 3, 4, 5] * 100000
        score = 0
        # 첫번째 학생
        for i in range(3):  # 학생마다 채점해야하니까, 학생번호
            for j in range(len(answers)):  # 문제 길이만큼
                if students_answers[i] == answers[i]:
                    score += 1
        scores.append(score)
        # 2 번째 학생
        students_answers = [2, 1, 2, 3, 2, 4, 2, 5] * 100000
        score = 0
        for i in range(3):  # 학생마다 채점해야하니까, 학생번호
            for j in range(len(answers)):  # 문제 길이만큼
                if students_answers[i] == answers[i]:
                    score += 1
        scores.append(score)
        # 3번째 학생
        students_answers = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 100000
        score = 0
        for i in range(3):  # 학생마다 채점해야하니까, 학생번호
            for j in range(len(answers)):  # 문제 길이만큼
                if students_answers[i] == answers[i]:
                    score += 1
        scores.append(score)
    
        # 위의 반복된 계산을 for 문으로 한번에 바꾸자 : 점수 계산
        scores = []
        patterns = [
            [1, 2, 3, 4, 5],
            [2, 1, 2, 3, 2, 4, 2, 5],
            [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
        ]
        for pattern in patterns:
            students_answers = pattern * 100000
            score = 0
            for i in range(len(answers)):
                if students_answers[i] == answers[i]:
                    score += 1
            scores.append(score)
    
        # 함수로 분리
        scores = []
        patterns = [
            [1, 2, 3, 4, 5],
            [2, 1, 2, 3, 2, 4, 2, 5],
            [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
        ]
        for pattern in patterns:
            score = calculate_score(pattern, answers)
            scores.append(score)
    
        # 고득점 학생 찾기
        max_score = max(scores)
        students = []
        for i in range(3):
            if scores[i] == max_score:
                students.append(i + 1)
    
        return students
    
    
    def calculate_score(pattern, answers):
        # students_answers = pattern * 100000
        # score = 0
        # for i in range(len(answers)):
        #     if students_answers[i] == answers[i]:
        #         score += 1
        # return score
    
        # students_answers = pattern * 100000
        # return sum(students_answers[i] == answers[i] for i in range(len(answers)))
    
        return sum(pattern[i % len(pattern)] == answers[i] for i in range(len(answers)))
    
    
    def test_sample():
        assert good_students([1, 2, 3, 4, 5]) == [1]

공공 데이터 DB에 넣기

[https://nbviewer.jupyter.org/github/ahastudio/CodingLife/blob/master/20191014/python/01-import-data.ipynb](https://nbviewer.jupyter.org/github/ahastudio/CodingLife/blob/master/20191014/python/01-import-data.ipynb)

공공 데이터 DB에서 가져오기

[https://nbviewer.jupyter.org/github/ahastudio/CodingLife/blob/master/20191014/python/02-use-data.ipynb](https://nbviewer.jupyter.org/github/ahastudio/CodingLife/blob/master/20191014/python/02-use-data.ipynb)