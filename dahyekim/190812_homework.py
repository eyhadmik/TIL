# 1) 두 개의 dictionary에서 국어 점수의 총 합은?
# => assert class_total(class_scores, '국어') == 170
# 이렇게 확인할 수 있는 함수를 만들어보세요
# 2) class_scores set에 있는 모든 점수의 합은 얼마인가요?
# => class_total_all(class_scores) == 430

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

def class_total(scores, subject):
    total = 0
    for dic in scores:
        total += dic[subject]
    return total


def class_total_all(scores):
    total = 0
    for dic in scores:
        for num in dic.values():
            total += num
    return total


def test_class_total():

    assert class_total(class_scores, '국어') == 80 + 90
    assert class_total(class_scores, '영어') == 100 + 70
    assert class_total(class_scores, '수학') == 50 + 40

def test_class_total_all():

    assert class_total_all(class_scores) == 80 + 100 + 50 + 90 + 70 + 40

