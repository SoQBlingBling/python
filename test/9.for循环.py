'''
for 临时变量 in 待处理数据集：
    遍历时执行代码

'''
money = 10000
import random
for i in range(1,21):
    f = random.randint(1,10)
    if f<5:
        print(f'员工{i}绩效分{f}不足5分不发放工资')    
        continue
    if money>=1000:
        money-= 1000    
        print(f'第{i}位员工发放工资1k，账户剩余{money}')
    else:    
        print('发完了下个月')
        break