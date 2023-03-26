import os
import string
import random
# 目前的port/生成规则和之前的sh脚本一致
current_path = os.getcwd()
parent_path = os.path.dirname(current_path)
traces_size = [1,4,16,256,1024,4096]#K
s = string.ascii_letters
for size_K in traces_size:
    file_name = parent_path + "/prototype/traces/file_size_"+str(size_K)+"K"+".data"
    data = ""
    for i in range(size_K*1024):
        data = data + random.choice(s)
    print(data)
    with open(file_name, 'w') as f:
        f.write(data)