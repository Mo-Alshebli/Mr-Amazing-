import numpy as np

X=[
    [1,1,1],
    [1,-1,1],
    [-1,1,1],
    [-1,-1,1]]

Y=[1,-1,-1,-1]
theta=1
output=0
sum=0
weight=[0,0,0]
while(True):
    for i in range(len(X)):

        for j in range(len(weight)):
           weight[j]=weight[j]+X[i][j]*Y[i]

    break
print(weight)

for i in range(len(X)):
    sum = 0
    for j in range(len(X[i])):
        sum += X[i][j] * weight[j]

    if sum < 0:
        output = -1
    else:
        output = 1
    print("output   ", output)


