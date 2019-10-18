class_score = [
    [40, 50, 60, 70, 80],
    [100, 100, 100, 100, 100],
    [20, 20, 20, 80, 70]
]

# class 전체 점수 총합
def total(scores):

    total_score = 0

    for i in range(len(scores)):
        for score in scores[i]:
            total_score += score
            # print(total_score)

    return total_score

# class 전체 점수 평균
def average(scores):
    total_length = 0

    for i in range(len(scores)):
        total_length += len(scores[i])

    avg_score = total(scores) / total_length

    return round(avg_score, 0)

# 각 개인별 점수 총합
def total_ind(scores):
    total_ind_list = []

    for i in range(len(scores)):
        total_score = 0
        for score in scores[i]:
            total_score += score
            # print(total_score)
        total_ind_list.append(total_score)

    return total_ind_list

# 각 개인별 점수 평균
def average_ind(scores):
    avg_ind_list = []

    for i in range(len(scores)):
        avg_ind_list.append(total_ind(scores)[i] / len(scores[i]))

    return avg_ind_list

print(total(class_score))
print(average(class_score))
print(total_ind(class_score))
print(average_ind(class_score))

