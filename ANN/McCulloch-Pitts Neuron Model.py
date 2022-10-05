import numpy as np

X = [
    [1, 1],
    [1, 0],
    [0, 1],
    [0, 0]
]

Y = [1, 0, 0, 0]
theta = 1
yn = 0
sum = 0.0
weight = np.random.uniform(0, 1, 2)
print("weight[w1,w2]",weight)
print('*****************************')
while (True):
    print("weight[w1,w2,b]", weight)
    print('*****************************')
    for i in range(len(X)):
        sum = 0
        for j in range(len(X[i])):
            sum += X[i][j] * weight[j]
        print('*****************************')
        print("The net is : ", sum)

        if sum < theta:
            yn = 0
        else:
            yn = 1
        print('*****************************')
        print("y",i+1," = ", yn)
    break


