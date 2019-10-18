from hw0819.py import grade, class_grades, update_class_grades

# Test Code
def test_grade():
    assert grade(100) == "A"
    assert grade(70) == "B"
    assert grade(50) == "C"
    assert grade(30) == "D"
    assert grade(0) == "F"
    assert class_grades([{'Korean': 100}], 'Korean') ==['A']
    assert class_grades([{'Korean': 90}], 'Korean') == ['A']
    assert class_grades([{'Korean': 70}], 'Korean') == ['B']
    assert class_grades([{'Korean': 90}, {'Korean': 70}], 'Korean') == ['A', 'B']

def test_update_class_grades():
    assert update_class_grades(class_scores, 'Korean')
    assert class_grades == [
        {'Korean': 100, 'Korean Grade': 'A'},
        {'Korean': 10, 'Korean Grade': 'F'}
    ]
    assert class_grades[0]['Korean Grade'] == 'A'
    assert class_grades[1]['Korean Grade'] == 'F'
