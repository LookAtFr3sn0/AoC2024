import pandas as pd

with open('inputs/day1.txt') as file:
    data = pd.read_csv(file, header=None, sep='  ', engine='python')

col1 = data[0]
col2 = data[1]

score = 0
counts = col2.value_counts()

for i in col1:
    score += i * counts.get(i, 0)

print(score)