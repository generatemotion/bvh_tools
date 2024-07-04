# import numpy as np

# input_string = "2020-06-30 23:59:59"
# output_tuple = np.sscanf(input_string, "%d-%d-%d %d:%d:%d")

# print(output_tuple)


import struct
 
def array_to_bytes(arr, t="i"):
    # 假设arr是一个整数列表
    return b''.join([struct.pack(t, num) for num in arr])
 
# 示例使用
int_array = [1.0, 2, 3, 4, 5]
bytes_seq = array_to_bytes(int_array,"f")
print(bytes_seq)
