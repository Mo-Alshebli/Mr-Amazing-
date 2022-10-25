import numpy as np
# input data
X = [
    [0, 0, 1, 1],
    [1, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 1]
]
# this learning rate
Learning_rate=0.5
# Enter how many clusters you want
clusters=int(input("Enter how many clusters you want : "))
# this loop for create initial matrix weight 
weight=[]
column=[]
for i in range(clusters):
    for j in range(len(X)):
        column.append(np.random.uniform(0,1))
    weight.append(column)
    column=[]
#convert the list of weight to array and X
weight=np.asarray(weight)
X=np.asarray(X)
output=[]
# weight=[[0.2,0.4,0.6,0.8],[0.9,0.7,0.5,0.3]]
# this for summtion 
summ=0.0
# here we calculate  the input and update the weight
for i in range(len(X)):
    output.clear()
    for j in range(len(weight)):
        summ = 0.0
        for l in range(len(weight[j])):
            summ+=np.square(weight[j][l]-X[i][l])
        output.append(summ)
    for a, k in enumerate(output):
        if k == min(output):
            for h in range(len(weight[a])):
                weight[a][h] = weight[a][h] + (Learning_rate * (X[i][h] - weight[a][h]))
            break
    
