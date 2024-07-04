import numpy as np
# list转矩阵
a=[[4,2],[3,2],[3,1]]
a =np.mat(a)
print("list转矩阵:", a)

# 矩阵转数组
a = a.A
print("矩阵转数组:", a)

print("数组转字节码:", a.tobytes())

str = "hello"
print("字符串转字节:", bytes(str, "utf8"))
b1=b"hello"
b2=b"world你好"
b=b1+b2
print("字节拼接:", b, len(b))
matrix_1 = np.mat([[7, 8, 9], [0, 5, 3]])
print("矩阵:",matrix_1)
# matrix([[7, 8, 9],
#         [0, 5, 3]])
# 矩阵转化为数组
array_1 = np.array(matrix_1)
print("数组:",array_1)
# array([[7, 8, 9],
#        [0, 5, 3]])
# 矩阵转化为列表
list_1 = matrix_1.tolist()
print("矩阵转数组:",list_1)
# [[7, 8, 9], [0, 5, 3]]
print("list_1.tobytes:", list_1.tobytes())
list_1 = list(matrix_1)
print(list_1)
# [matrix([[7, 8, 9]]), matrix([[0, 5, 3]])]
