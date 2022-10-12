import numpy as np
#============ tis function for convert from 2dim to one
def re(x):
    E=[]
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            E.append(x[i][j])
    return E
#========== this for return the activation function 1
def act(x):
    for j in range(x.shape[0]):
        for i in range(x.shape[1]):
            if x[j][i] > 0:
                x[j][i] = 1
            elif x[j][i] < 0:
                x[j][i] = -1
            else:
                x[j][i] = 0

    return x

#========== this for return the activation function 2

def act2(x):
    for j in range(x.shape[0]):
        if x[j] > 0:
            x[j] = 1
        elif x[j] < 0:
            x[j] = -1
        else:
            x[j] = 0


    return x


E_input = np.array([
    [1, 1, 1],
    [1, -1, -1],
    [1, 1, 1],
    [1, -1, -1],
    [1, 1, 1]
])
F_input = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, -1, -1],
    [1, -1, -1],
    [1, -1, -1]
])

# ========= the target value ============
E_input_=[-1,1]
F_input_=[1,1]

#  ==========transpose the target to multiply with inout =====
E_output=np.array([[-1,1]]).T
F_output=np.array([[1,1]]).T
# ========= convert the input array from multi dim to one
E=np.array([re(E_input)])
F=np.array([re(F_input)])

# ========== calculate  the weight by multiply the input and output using the function matmul in numpy
W_E_=np.matmul(E_output,E)
W_E=np.array(W_E_).T
W_F_=np.matmul(F_output,F)
W_F=np.array(W_F_).T

#  ===========  adding the tow weight to get the final weight to use it in test
e=W_E+W_F

#  ===========multiply the input and final weight to test if we will get the correct output
E_yin=np.array(np.matmul(E,e))
F_yin=np.array(np.matmul(F,e))

#  ======= useing the activation function of bipolr
E_yin=act(E_yin)
F_yin= act(F_yin)

# ======== multiply the output with final weight to get the input and check  if it is correct
E_yin_T=np.matmul(E_input_,W_E_)
F_yin_T=np.matmul(F_input_,W_F_)

#  ======= useing the activation function of bipolr

E_yin_T=act2(E_yin_T)
F_yin_T=act2(F_yin_T)
