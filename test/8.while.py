# 基本语法
# a = 0
# while a<10:
#     print(a)
#     a+=1

"""

打印99乘法表

"""
i = 1
while i<=9:
    j = 1
    while j<=i:
        print(f'{j}×{i}={i*j}\t',end='')
        j+=1
    print()  
    i+=1