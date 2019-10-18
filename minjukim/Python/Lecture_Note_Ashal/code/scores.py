def class_total(class_scores, subject):
    total_score = 0
    for score in class_scores:
        total_score += score[subject]
    return total_score

def class_avg(class_scores, subject):
    avg_score = class_total(class_scores, subject) / len(class_scores)
    return avg_score