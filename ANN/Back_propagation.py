

#تم بناء البرنامج بناء على قيم افتراضية بلامكان التغير على  حسب المسائلة المراد حلها
#   يتم التعديل في المدخلات والمخرجات والاوزان
import numpy as np
# the first tow value is the input  to the networks and the third value is value of bias 
X=[
   [0,0,1],
   [0,1,1],
   [1,0,1],
   [1,1,1]]
# this the output that we want to get it at last of training
T=[0,1,1,0]
#this the value of error that we want the network stop when they return  to this value
err=0.5094
# this we initial the wright with this value you can change it as you need 
w13,w23,wb3,w14,w24,wb4,w35,w45,wb5=0.3,-0.1,0.2,-0.2,0.2,-0.3,0.4,-0.2,0.4
# we make this  step for split all neurons with their weight
W=[[w13,w23,wb3],[w14,w24,wb4],[w35,w45,wb5]]
# we initially the o that activation function results 
o=[0.0,0.0,1]
# this the return value of delta O the input neuron 
do=[0.0,0.0,0.0]
# initial the Y 
y=0.0
#this for the return value of  delta Y the hidden layer
dy=0.0
# this value of alpha
a=0.3
# the initial of error 
sum_Err=1
#this for how many epochs you  want  to do 
in_epoch=int(input("Enter how many epoch you wnt to do : "))
#this Function for calculate the net  and applied  the activation function sigmid in return the function
def Net(x,w):
    net= w[0]*x[0]+w[1]*x[1]+w[2]
    return 1/(1+np.exp(-net))
# this for calculate the Errors 
def Error(net,t):
    return 0.5*(t-net)**2

 # this for calculate the Delta Y 
def Delta_y(t,y):
    return y*(1-y)*(t-y)
 # this for calculate the Delta O
def Delta_o(o,o5,w):
    return o*(1-o)*o5*w
# this for updates the weights
def update_weight(w,a,x,d):
    for j in range(len(w)):
        w[j]=w[j]+a*x[j]*d
    return w

epochs=0

while True:
   # this condition if the error we get less than the initial error we will stop
    if sum_Err < err or in_epoch==epochs:
        print(epochs)
        break
    else:
      
        sum_Err=0.0
         # this for its for forward 
        for i in range(len(X)):
            for j in range(len(o)):
                o[j] = Net(X[0], W[j])
            y = Net(o, W[2])
            sum_Err += Error(y,T[i])

            dy=Delta_y(T[i],y)
            # this for its for backward 
            for j in range(len(o)):
                do[j]=Delta_o(o[j],dy,W[2][j])
            do[2]=dy
            for j in range(len(W)):
                W[j]=update_weight(W[j],a,X[i],do[j])
    epochs+=1

print(W)
print(sum_Err)
