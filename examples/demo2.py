# print ("He is %d years old, and %s" % (23, 'hello world')) 
# print("he is %d old"% 12)
import re
def trim(str):
    """
    remove all type of blank space
    """
    if str is None:
        return ""
    else:
        tmp = re.sub('\s|\t|\n', ' ', str)
        tmp = tmp.strip()
        tmp = "".join(tmp.split())
        return tmp

str = "Frames:    2"
t = str.split(" ")
print(t)
t = ''.join(t)
print(t)
print(trim(str))