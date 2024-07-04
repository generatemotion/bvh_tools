# https://hg95.github.io/numpy-pandas-scipy/Chapter1/NumPy%20%E7%9F%A9%E9%98%B5%E5%BA%93Matrix.html

import glm
import numpy as np
from numpy import random, mat,eye
import numpy.matlib

matA = np.mat([[1, 2],[3, 4]])
matB = np.array([[1, 2], [3, 4]])

print('A*B \n', matA*matB)
print('np.dot(A,B)\n', np.dot(matA,matB))
print('multiply \n', np.multiply(matA,matB))

# ndarray与matrix转换
r_arr=random.rand(4,4)
print('r_arr',r_arr)
r_mat=mat(r_arr)
print(r_mat.I)#求逆

# matrix 转换array
# 直接使用matrix A 属性， 即 matrix.A.
mat = np.mat([[1,2],[3,4]])
print('mat type:{}, \n mat:\n{}'.format(type(mat), mat))

arr = mat.A
print('arr type:{}, \n arr:\n{}'.format(type(arr),arr))

print("arr:", arr.tobytes())

# matlib.empty() 函数返回一个新的矩阵，语法格式为： numpy.matlib.empty(shape, dtype, order)
# 返回给定形状和类型的新矩阵，而不初始化条目。
# 参数说明：
# shape: 定义新矩阵形状的整数或整数元组
# Dtype: 可选，数据类型
# order: C（行序优先） 或者 F（列序优先）
a = np.matlib.empty((2, 2))    # filled with random data
print(a)

a = np.matlib.empty((2, 2), dtype=int)
print(a)

# numpy.matlib.zeros() 函数创建一个以 0 填充的矩阵。
# shape：int或ints序列矩阵的形状
# dtype：数据类型，可选矩阵的所需数据类型，默认为float。
# order：{'C'，'F'}，可选是否以C或Fortran连续顺序存储结果，默认值为“C”。
# 如果shape具有长度一即(N,)或者是标量N，则out形状矩阵(1,N)。
b = np.matlib.zeros((2, 3))

c = np.matlib.zeros(2)

d = np.matlib.ones((2,3))

e = np.matlib.ones(2)

# numpy.matlib.eye() 函数返回一个矩阵，对角线元素为 1，其他位置为零。
# numpy.matlib.eye(n, M,k, dtype) 参数说明：
# n: 返回矩阵的行数
# M: 返回矩阵的列数，默认为 n
# k: 对角线的索引 , 0表示主对角线，正值表示上对角线，负值表示下对角线。
# dtype: 数据类型
np.matlib.eye(3, k=1, dtype=float)

# numpy.matlib.identity(n,dtype=None)函数返回给定大小的单位矩阵。

# 单位矩阵是个方阵，从左上角到右下角的对角线（称为主对角线）上的元素均为 1，除此以外全都为 0。

# n：int 返回的单位矩阵的大小。

# dtype：数据类型，可选 输出的数据类型。默认为float。
np.matlib.identity(3, dtype=int)

# numpy.matlib.rand(*args)函数创建一个给定大小的矩阵，数据是随机填充的。

# 返回具有给定形状的随机值矩阵。

# 创建给定形状的矩阵，并通过[0， 1）的均匀分布的随机样本传播它。

# * args：参数

# 输出形状。如果给定为N个整数，每个整数指定一个维度的大小。如果给出一个元组，这个元组给出完整的形状。
np.matlib.rand(2, 3)

# 将输入解释为矩阵。

# numpy.mat(data, dtype=None)

# data：array_like 输入数据。

# dtype：数据类型 输出矩阵的数据类型。
from numpy import *

a1=array([1,2,3]) # 数组
print("shape==>",shape(a1))
a1=mat(a1) # 矩阵
shape(a1) #(1,3)

# 常见矩阵
data1 = mat(zeros((3,3))) #创建一个3*3的零矩阵，矩阵这里zeros函数的参数是一个tuple类型(3,3)
data2=mat(ones((2,4))) #创建一个2*4的1矩阵，默认是浮点型的数据，如果需要时int类型，可以使用dtype=int
data3=mat(random.rand(2,2)) #这里的random模块使用的是numpy中的random模块，random.rand(2,2)创建的是一个二维数组，需要将其转换成#matrix

data4=mat(random.randint(10,size=(3,3))) #生成一个3*3的0-10之间的随机整数矩阵，如果需要指定下界则可以多加一个参数

data5=mat(random.randint(2,8,size=(2,5))) #产生一个2-8之间的随机整数矩阵

data6=mat(eye(2,2,dtype=int)) #产生一个2*2的对角矩阵

a1=[1,2,3]
a2=mat(diag(a1)) #生成一个对角线为1、2、3的对角矩阵

# 矩阵乘法
a1=mat([1,2]);      
a2=mat([[1],[2]]);
a3=a1*a2;
#1*2的矩阵乘以2*1的矩阵，得到1*1的矩阵

# 矩阵点乘
a1=mat([3,1])
a2=mat([2,2])
a3=multiply(a1,a2)
# matrix([[6, 2]])

# 矩阵求逆
a1=mat(eye(2,2)*0.5)
a2=a1.I  #求矩阵matrix([[0.5,0],[0,0.5]])的逆矩阵

# 矩阵转置
a1=mat([[1,1],[0,0]])
a2=a1.T

# 矩阵的分隔
a=mat(ones((3,3)))
b=a[1:,1:]  #分割出第二行以后的行和第二列以后的列的所有元素
# 矩阵合并
a=mat(ones((2,2)))
# matrix([[ 1.,  1.],
#         [ 1.,  1.]])

b=mat(eye(2))
# matrix([[ 1.,  0.],
#         [ 0.,  1.]])
c=vstack((a,b))  #按列合并，即增加行数
# matrix([[ 1.,  1.],
#         [ 1.,  1.],
#         [ 1.,  0.],
#         [ 0.,  1.]])

# 扩展矩阵函数tile()
# tile(inX, (i,j)) ;i是扩展个数，j是扩展长度
x=mat([0,0,0])
# matrix([[0, 0, 0]])
tile(x,(3,1))           #即将x扩展3个，j=1,表示其列数不变
# matrix([[0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0]])
tile(x,(2,2))           #x扩展2次，j=2,横向扩展
# matrix([[0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0]])

matrix_1 = np.mat([[7, 8, 9], [0, 5, 3]])
# matrix_1
# matrix([[7, 8, 9],
#         [0, 5, 3]])
# 矩阵转化为数组
array_1 = np.array(matrix_1)
# array_1
# array([[7, 8, 9],
#        [0, 5, 3]])
# 矩阵转化为列表
list_1 = matrix_1.tolist()
# list_1
# [[7, 8, 9], [0, 5, 3]]

list_1 = list(matrix_1)
# >>> list_1
# [matrix([[7, 8, 9]]), matrix([[0, 5, 3]])]
