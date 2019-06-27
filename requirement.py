# import os, sys
#
# # 找到当前目录
# project_root = os.path.dirname(os.path.realpath(__file__))
# print(project_root)
#
# # 找到解释器，虚拟环境目录
# python_root = sys.exec_prefix
# print(python_root)
#
# # 拼接生成requirements命令
# command = python_root + '\Scripts\pip freeze > ' + project_root + '\\requirements.txt'
# print(command)
#
# # 执行命令。
# os.system(command)
def fibonacci(num):
    i,a,b= 0,0,1
    if int(num) < 0:
        print("你输入的数据不合理")
    elif int(num)== 1:
        print(a)
    else:
        while i < int(num):
            #sum  = a+b
            #a = b
            #b = sum
            a, b = b, a + b  #a, b = b, a + b这里不能写成 a=b   b=a+b，如果写成这样，b就不是前两位相加的值，而是已经被b赋过值的a和b相加的值
            i+=1
        print(a)
import time
t1 = time.time()
print(t1)
fibonacci(100000)
t2 = time.time()
print(t2)
print(t2-t1)