import pandas as pd

with open('inputs/day1.txt') as file:
    data = pd.read_csv(file, header=None, sep='  ', engine='python')

col1 = data[0].sort_values().values
col2 = data[1].sort_values().values

distance = 0

for i in range(len(col1)):
    distance += abs(col1[i] - col2[i])

print(distance)