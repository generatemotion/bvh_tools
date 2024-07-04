# import numpy as np
# flatgeom_np = np.array([1.0,2.0,0.0])
# #            print (flatgeom_np)
# bin_geom = flatgeom_np.astype(np.uint32).tostring()
# print(bin_geom)
# print(len(bin_geom))
import glm

# 目的：把一个向量(1, 0, 0)位移(1, 1, 0)个单位
# 1、定义该向量 vec
vec = glm.vec4(1.0, 0.0, 0.0, 1.0);
# 2、初始化一个单位矩阵
trans = glm.mat4(1.0)
print("trans==", trans)
# 3、将向量(1, 1, 0)与单位矩阵相乘
trans = glm.translate(trans, glm.vec3(1.0, 1.0, 0.0));

print("trans==", trans)

# //4、将结果再与最初的向量相乘，来对其进行位移改变
vec = trans * vec;
print("vec==",vec)
