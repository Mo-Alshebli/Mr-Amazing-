import numpy as np

input_=np.array([[1, -1, -1, -1],
        [1,1,-1,-1],
        [-1,-1,-1,1],
        [-1,-1,1,1]])

output=np.array([
        [-1,1],
        [-1,1],
        [1,-1],
        [1,-1]])

# =================== Train ang get weight ============
train = np.array(input_).T
weight=np.matmul(train,output)
print(' the weight is :\n ',weight,'\n')

# ================== to test if your train is done well ================
# testw=[]
# for i in range(input_.shape[0]):
#     test=np.matmul(input_[i],weight)
#     # print(test.shape[0])
#     for j in range(test.shape[0]):
#         if test[j]>0:
#             test[j]=1
#         elif test[j]<0:
#             test[j]=-1
#         else:
#             test[j]=0
#     testw.append(test)
#
# test=np.array(testw)
# e=np.array_equal(output,test)
# print(' The result of train  all of it is   : ',e)

# =================== test ====================
u=[0,1,0,-1]
test_ = np.matmul(u, weight)
for j in range(test_.shape[0]):
    if test_[j] > 0:
        test_[j] = 1
    elif test_[j] < 0:
        test_[j] = -1
    else:
        test_[j] = 0
print('the row that we want to test it is : ',u)
print('The result after testing is : ',test_)



