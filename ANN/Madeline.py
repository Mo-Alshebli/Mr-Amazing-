import numpy as np

X = [
    [1, 1],
    [1, -1],
    [-1, 1],
    [-1, -1],
]
Y = [-1, 1, 1, -1]
Zw1, Zw2, bais = [0.05, 0.2], [0.1, 0.2], [0.3, 0.15]
learning_rate = 0.5
zin1 = 0.0
zin2 = 0.0
b = 0.0
y=0.5
counter=0
ch=0
for n in range (1000):

    for i in range (len(X)):
        counter+=1
        check = 0
        WZ11,WZ22,bais_Old=[Zw1[0],Zw1[1]],[Zw2[0], Zw2[1]], [bais[0],bais[1]]
        zin1 = bais[0] + (X[i][0] * Zw1[0]) + (X[i][1] * Zw1[1])
        zin2 = bais[1] + X[i][0] * Zw2[0] + X[i][1] * Zw2[1]

        net = [round(zin1, 3), round(zin2, 3)]
        in_val, idx = min([(abs(val), idx) for (idx, val) in enumerate(net)])
        if zin1 >= 0:
            zin1 = 1
        else:
            zin1 = -1
        if zin2 >= 0:
            zin2 = 1
        else:
            zin2 = -1
        y = y + zin1 * y + zin2 * y
        if y >= 0:
            y = 1
        else:
            y = -1

        if Y[i] != y:
            if Y[i] == 1:
                if in_val == abs(net[0]):
                    for j in range(len(Zw1)):
                        Zw1[j] = Zw1[j] + (learning_rate * (1 - net[0]) * X[i][j])
                       

                    bais[0] = bais[0] + learning_rate * (1 - net[0])

                else:
                    for j in range(2):
                        Zw2[j] = Zw2[j] + (learning_rate * (-1 - net[1]) * X[i][j])
                    bais[1] = bais[1] + learning_rate * (-1 - net[1])
            elif Y[i] == -1:
                if zin1 > 0 and zin2 > 0:
                    for j in range(2):
                        Zw1[j] = Zw1[j] + (learning_rate * (Y[i] - net[0]) * X[i][j])
                        Zw2[j] = Zw2[j] + (learning_rate * (Y[i] - net[1]) * X[i][j])
                        bais[j] = bais[j] + learning_rate * (Y[i] - net[j])
                elif zin1 > 0:
                    for j in range(len(Zw1)):
                        Zw1[j] = Zw1[j] + (learning_rate * (Y[i] - net[0]) * X[i][j])
                        bais[0] = bais[0] + learning_rate * (Y[i] - net[0])


                elif zin2 > 0:
                    for j in range(len(Zw1)):
                        Zw2[j] = Zw2[j] + (learning_rate * (Y[i] - net[1]) * X[i][j])
                        bais[1] = bais[1] + learning_rate * (Y[i] - net[1])

        for c in range (2):
            if WZ11[c]==Zw1[c] and WZ22[c]==Zw2[c] and bais[c]==bais_Old[c] :
                check+=1
        if check==2:
            ch+=1
        else :
            ch=0
        print("last : ", WZ11, WZ22, bais_Old)
        print("New",Zw1,Zw2,bais)

    if ch>1000:
        print(counter-ch)
        break



