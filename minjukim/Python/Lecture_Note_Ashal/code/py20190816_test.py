from py20190816 import select_high_scores

def test_select_high_scores():
    assert select_high_scores([]) == []
    assert select_high_scores([60]) == [60]
    assert select_high_scores([60, 0]) == [60]
    assert select_high_scores([50, 50]) == [50, 50]

test_select_high_scores()