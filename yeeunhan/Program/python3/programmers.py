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
