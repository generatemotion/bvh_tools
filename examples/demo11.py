import glm

matrix = glm.mat4(2.0)
print("mat4:", matrix)
rotate = glm.quat_cast(matrix)
print(rotate,rotate[0])