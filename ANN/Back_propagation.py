

#تم بناء البرنامج بناء على قيم افتراضية بلامكان التغير على  حسب المسائلة المراد حلها
#   يتم التعديل في المدخلات والمخرجات والاوزان
import numpy as np

X=[
   [0,0,1],
   [0,1,1],
   [1,0,1],
   [1,1,1]]

T=[0,1,1,0]
err=0.5094
w13,w23,wb3,w14,w24,wb4,w35,w45,wb5=0.3,-0.1,0.2,-0.2,0.2,-0.3,0.4,-0.2,0.4
W=[[w13,w23,wb3],[w14,w24,wb4],[w35,w45,wb5]]
o=[0.0,0.0,1]
do=[0.0,0.0,0.0]
y=0.0
dy=0.0
a=0.3
sum_Err=1



in_epoch=int(input("Enter how many epoch you wnt to do : "))


def Net(x,w):
    net= w[0]*x[0]+w[1]*x[1]+w[2]
    return 1/(1+np.exp(-net))

def Error(net,t):
    return 0.5*(t-net)**2

def Delta_y(t,y):
    return y*(1-y)*(t-y)

def Delta_o(o,o5,w):
    return o*(1-o)*o5*w

def update_weight(w,a,x,d):
    for j in range(len(w)):
        w[j]=w[j]+a*x[j]*d
    return w

epochs=0
while True:
    if sum_Err < err or in_epoch==epochs:
        print(epochs)
        break
    else:
        sum_Err=0.0
        for i in range(len(X)):
            for j in range(len(o)):
                o[j] = Net(X[0], W[j])
            y = Net(o, W[2])
            sum_Err += Error(y,T[i])

            dy=Delta_y(T[i],y)
            for j in range(len(o)):
                do[j]=Delta_o(o[j],dy,W[2][j])
            do[2]=dy
            for j in range(len(W)):
                W[j]=update_weight(W[j],a,X[i],do[j])
    epochs+=1

print(W)
print(sum_Err)









