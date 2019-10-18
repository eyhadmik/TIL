class_scores = [
    {
        '국어': 80,
        '영어': 100,
        '수학': 50
    },
    {
        '국어': 90,
        '영어': 70,
        '수학': 40
    }
]
# print(class_scores[0]['국어'])

# 20점 단위 A-F 학점
# A: 100-80
# B: 80-60
# C: 60-40
# D: 40-20
# F: 20-0
# 테이블로 표시
# github

print(class_scores[0]['국어'])

#
# def class_grade(scores):
#     # if score == {'국어' : 90}:
#     #     return 'A'
#     # elif score == {'국어': 70}:
#         # return 'B'
#     if scores['국어'] >= 80:
#         return 'A'
#     elif scores['국어'] >= 60:
#         return 'B'
#     elif scores['국어'] >= 40:
#         return 'C'
#     elif scores['국어'] >= 20:
#         return 'C'
#     else:
#         return 'F'

# A= {'a':1, 'b':2}
# print(A['a'])