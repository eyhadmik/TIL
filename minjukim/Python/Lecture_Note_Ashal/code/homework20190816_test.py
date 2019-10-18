from homework20190816 import class_grade

def test_class_grade():
    # assert class_grade([{}, {}]) == 'F'
    # assert class_grade([{'국어': 80, '영어': 100}, {'국어': 90}]) == {'국어':'A'}
    assert class_grade([{'국어': 80}, {'국어': 90}]) == [{'국어': 'A'}, {'국어': 'A'}]

test_class_grade()