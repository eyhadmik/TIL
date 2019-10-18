def grade(score):
    # 비정상처리를 맨 위에 쓴다
    # Guard Cross
    if score < 0 or score > 100:
        return "Please Check the Score"

    # 1. 일반적인 for 문
    grades = {
        'A': 80,
        "B": 60,
        'C': 40,
        'D': 20
    }
    # for grade in grades:
    #     if score >= grades[grade]:
    #         return grade

    # 2. dictionary method 를 쓰는 for 문
    # dictionary.items()
    # key 값과 value 값이 함께 나온다
    for grade, min_score in grades.items():
        if score >= min_score:
            return grade

    # 0. if 문으로 풀기
    # if score >= 80:
    #     return "A"
    # if score >= 60:
    #     return "B"
    # if score >= 40:
    #     return "C"
    # if score >= 20:
    #     return "D"

    return "F"

# 4. 소름; 한 줄로 끝나는 코드
#    return 'FDCBAA'[score // 20]

# 코드 작동 과정
# score = 100 점일 때
# 'FDCBAA'[100 // 20]
# 'FDCBAA'[5]
# 앞의 List 에서 5번째 값 출력
# 'A'

# ['Student1', 'Student2']
#
# [
#     {'Korean': 80, 'English': 100, 'Math': 20},
#     {'Korean': 80, 'English': 100, 'Math': 20}
# ]

def class_grades(class_scores, subject):
    if len(class_scores) == 0:
        return []
    # scores = class_scores[0]
    # score = scores[subject]
    # return [grade(score)]

    # 초기값
    grades = []
    # 누산
    for scores in class_scores:
        score = scores[subject]
        grades.append(grade(score))
    # 리턴
    return grades


def update_class_grades(class_scores, subject):
    grades = class_grades(class_scores, subject)

    for i in range(len(class_scores)):
        class_scores[i][f'{subject} Grade'] = grades[i]

update_class_grades()