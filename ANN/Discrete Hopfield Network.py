import numpy as np


def act(x):
    if x > 0:
        x = 1
    elif x < 0:
        x = -1
    else:
        x = 0

    return x


bb = np.array([1, 1, 1, -1])
dd = np.array([[1, 1, 1, 0]]).T
input_ = np.array([1, 1, 1, 0])
#  the weight = 2*dd-1,2*in_-1
in_ = np.array([input_])
Weight = np.matmul(2 * dd - 1, 2 * in_ - 1)

for j in range(Weight.shape[0]):
    for i in range(Weight.shape[1]):
        if i == j:
            Weight[j][i] = 0

X = Y = np.array([0, 0, 1, 0])
r = np.array([0, 1, 2, 3])
np.random.shuffle(r)
print('Weight : \n',Weight,'\n')

for i in r:
    W = np.array([Weight[i]]).T
    sum_ = np.matmul(Y, W)
    yin = X[i] + sum_
    yin = act(yin)
    Y[i] = yin
    m = 0
    for j in range(bb.shape[0]):
        if Y[j] == bb[j]:
            m = m + 1

    if m == 4:
        print(i, Y)
        print('done')
        break
