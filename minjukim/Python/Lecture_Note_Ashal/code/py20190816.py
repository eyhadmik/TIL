def select_high_scores(scores):
    high_scores = []
    for score in scores:
        if score >= 50:
            high_scores.append(score)

    return high_scoress