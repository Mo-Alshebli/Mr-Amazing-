# library required for program 
import  numpy as np
#The  input value
X=[
    [1,1],
    [1,-1],
    [-1,1],
    [-1,-1]
]
#The output we want to get it
Y=[-1,1,-1,-1]
# the weight of bias input
wb=0.2
# the initial value  of alpha
alpha=0.2
#the initial value of summation the input and weights 
sum=0
# the initial value of weight with random value
weight=np.random.uniform(0,1,2)
# the initial value of error
error=0.0
# this loop for epochs  start from 1 to 100 epochs
for k in range(1,100):
    print("weight[w1,w2]= ", weight,"   W_bais = ",wb)
    print('********************************************')
    # this loop for iteration 
    for i in range(len(X)):
        lerr=error
        sum = wb
        #this loop for calculate the summation
        for j in range(len(X[i])):
            sum += X[i][j] * weight[j]

        print(lerr)
        #this for calculat the error 
        error=pow(sum-Y[i],2)
        # this condition change the weight if Y[i] not equal 0 change it
        if Y[i]-sum!=0:
            #this for calculate the new weight 
            for j in range(len(weight)):
                weight[j] = weight[j] + X[i][j] * (Y[i]-sum)*alpha
             # calculate  the bias weight
            wb=wb+ (Y[i]-sum)*alpha
    print("The net is : ",sum)
    print('********************************************')
#this for stop  the  the loop of epochs 
    if lerr==error:
        print(k)
        print("Done")
        break
