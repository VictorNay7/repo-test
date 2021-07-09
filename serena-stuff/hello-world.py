import pandas as pd

print('Hello World')

grades = pd.read_csv('grades.csv')

grade_pivot = grades.pivot(
    columns="test",
    index="student",
    values="grade"
)

print(grade_pivot)