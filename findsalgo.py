import pandas as pd
import numpy as np

data = pd.read_csv('tennis.csv')
data.head()

d = np.array(data)[:, :-1]  # all the rows, all the columns except last 1
print("n The attributes are: ", d)

target = np.array(data)[:, -1]  # all the rows, last clumn only
print("n The target is: ", target)

def train(c, t):
    specific_hypothesis=[]
    for i, val in enumerate(t):
        if val == "Yes":
            specific_hypothesis = c[i].copy()
            break
    for i, val in enumerate(c):
        if t[i] == "Yes":
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    specific_hypothesis[x] = '?'
                else:
                    pass

    return specific_hypothesis
print("n The final hypothesis is:", train(d, target))
