from hw0819 import update_class_grades

def main():
    class_scores = [
        {'Name':'Jane', 'Korean':100, 'English':100, 'Math':100},
        {'Name':'Brown', 'Korean':10, 'English':20, 'Math':30},
        {'Name':'Susan', 'Korean':90, 'English':70, 'Math':50}
    ]

    update_class_grades(class_scores, 'Korean')
    update_class_grades(class_scores, 'English')
    update_class_grades(class_scores, 'Math')

    columns = [
        'Korean Grade', 'Korean',
        'English Grade', 'English',
        'Math Grade', 'Math'
    ]

    table = pd.DataFrame(class_scores, columns=columns)
    print(table)

main()