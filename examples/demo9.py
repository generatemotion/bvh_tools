import glm
import pymat

# a=glm.mat4(1.0)
# a=3*a
# print(a)
# arr = glm.array((a))
# print(arr,arr.to_bytes())
# a=pymat.mat4(2.0)
# print("a=",a)
# a=pymat.mat3(3.0)
# print("a=",a)

# print("a's bytes==", pymat.tobytes(a))

# print("a's inverse==", pymat.inverse(a))
import re
def trim(str):
    """
    remove all type of blank space
    """
    if str is None:
        return ""
    else:
        tmp = re.sub('\s|\t|\n', ' ', str)
        print(tmp)
        tmp = tmp.strip()
        print(tmp)
        tmp = " ".join(tmp.split())
        print(tmp)
        return tmp
from scanf import scanf
line="                                         OFFSET   0.00   -11.96   0.00"
tmp = scanf("%s %f %f %f", trim(line))
# print("OFFSET==line==>", line, tmp,trim(line))
