import pandas as pd

from scores import class_total
from scores import class_avg

def main():
    class_scores = [
        {'Name': 'Jane', 'Korean': 100, 'English': 100, 'Math': 100},
        {'Name': 'Brown', 'Korean': 10, 'English': 20, 'Math': 30}
    ]

    total = {'Name': '<Total>'}
    for subject in ['Korean', 'English', 'Math']:
        total[subject] = class_total(class_scores, subject)

    avg = {'Name': '<Average>'}
    for subject in ['Korean', 'English', 'Math']:
        avg[subject] = class_avg(class_scores, subject)

    table = pd.DataFrame(class_scores + [total] + [avg],
                         columns=['Name', 'Korean', 'English', 'Math'])

    table["Average"]
    table["Total"]

    print(table)


main()


