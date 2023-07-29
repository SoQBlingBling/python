# def say_hi(name):
#     print(f'你好啊，{name}')

# say_hi('张三')

# def sum(a,b):
#     print(a,b)

# print(sum(1,2))

money = 1000
name  = input('请输入姓名')
# 查询余额
def balance():
    print(f'当前余额{money}')
    menu()
# 存款
def deposit():
    num = int(input('请输入取款金额'))
    global money
    money +=num
    print(f'当前余额{money}')
    menu()
#取款
def withdraw_money():
    num = int(input('请输入存款金额'))
    global money
    if money>num:
        money-=num
        print(f'当前余额{money}')
    else:
        return    
    menu()
#主菜单
def menu():
    print('1.查询\n2.存款\n3.取款\n4.主菜单')
    num = int(input('请选择功能'))
    if num==1:
       balance()
    elif num ==2:
        deposit()    
    elif num ==3:
        withdraw_money()
    elif num ==4:    
        menu()
    else:
        return    
menu()