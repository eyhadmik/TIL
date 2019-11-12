
scores = [80, 100, 70, 90, 40]

def total(scores):
    total_score = 0
    for i in range(len(scores)):
        total_score += scores[i]
    return total_score

def average(scores):
    avg = total(scores) / len(scores)
    return avg

def test_():
    assert total(scores) == 380
    assert average(scores) == 76
