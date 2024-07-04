# for (i in range(10)):
#     print("php.cn")
# data = [0.0]
# str = "".join(data)
# print(str)
import re
def trim(str):
    """
    remove all type of blank space
    """
    if str is None:
        return ""
    else:
        tmp = re.sub('\s|\t|\n', ' ', str)
        # print(tmp)
        tmp = tmp.strip()
        # print(tmp)
        tmp = " ".join(tmp.split())
        # print(tmp)
        return tmp
# s = trim("ROOT Hips")
# print(s)

from scanf import scanf
line = "CHANNELS 6 Xposition Yposition Zposition Zrotation Xrotation Yrotation"
line = "OFFSET	0.00	0.00	0.00"
tmp = scanf("%s %f %f %f", trim(line))
print(tmp,tmp[0],tmp[1])