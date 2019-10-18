def total(scores):
    total_score = 0
    for score in scores:
        total_score += score
    return total_score

def average(scores):
    avg_score = total(scores) / len(scores)
    return avg_score

my_scores = [80, 100, 70, 90, 40]
print(total(my_scores))
print(average(my_scores))
