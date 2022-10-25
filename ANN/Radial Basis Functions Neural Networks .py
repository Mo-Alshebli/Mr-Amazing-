import numpy as np
import matplotlib.pyplot as pl
# input data
X = [
    [0, 0],
    [1, 0],
    [0, 1],
    [1, 1]

]
Y = [0, 1, 1, 0]

# this function include Gaussian role and equliden role
def Gaussian(x1, x2, alph):
    x = np.sqrt(np.square(x1[0] - x1[1]) + (np.square(x2[0] - x2[1])))

    d = (-1 * (np.square(x))) / (2 * np.square(alph))
    return np.exp(d)

# you should Enter the center point you want
point = int(input("Enter how many  points you want to put it in centers :"))
a = np.arange(point)
# we will append the point after insert it to the function
f = []
for i in a:
    for j in range(len(X)):
        f.append(Gaussian(X[i], X[j], 1))

    if point > len(X):
        break
# this for print and plot the output
if point <= len(X):
    print("    Q1    |       Q2    |    Q3    |     Q4")
    print("===================================================")
    d = np.asarray(f).reshape(4, point)
    print(d)
    fig = pl.figure()
    ax = fig.add_subplot(111, projection='3d')
    img = ax.scatter(d[0], d[1], d[2], c=d[3], cmap='BrBG_r', alpha=1)
    pl.show()
else:
    print(f" the point should be less than : {len(X)}")
