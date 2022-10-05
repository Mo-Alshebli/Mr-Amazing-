import  numpy as np

X=[
    [1,1],
    [1,-1],
    [-1,1],
    [-1,-1]
]

Y=[-1,1,-1,-1]
wb=0.2
alpha=0.2
yn=0
sum=0
weight=np.random.uniform(0,1,2)
error=0.0
for k in range(1,100):
    print("weight[w1,w2]= ", weight,"   W_bais = ",wb)
    print('********************************************')
    for i in range(len(X)):
        lerr=error
        sum = wb
        for j in range(len(X[i])):
            sum += X[i][j] * weight[j]

        print(lerr)
        error=pow(sum-Y[i],2)

        if Y[i]-sum!=0:
            for j in range(len(weight)):
                weight[j] = weight[j] + X[i][j] * (Y[i]-sum)*alpha
            wb=wb+ (Y[i]-sum)*alpha
    print("The net is : ",sum)
    print('********************************************')

    if lerr==error:
        print(k)
        print("Done")
        break
