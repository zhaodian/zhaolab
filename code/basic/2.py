def add(para1, para2):
    return para1 + para2
'''
def：定义函数
add：函数名
()：里面放参数，就是调用方(谁用这个函数)告诉函数的信息
return：返回给调用方的内容
上面这个函数定义说成人话就是：
我们造了一个函数，它的名字叫add，能接受2个参数para1、para2，
函数把para1、para2的值相加后，返回给了调用方
'''

a = 1			# 将1赋值给变量a
b = 2			# 将2赋值给变量b
c = add(a, b)	
# 将变量a、变量b的值赋给add函数的参数para1、para2
# 函数add将para1、para2相加的值返回并赋值给变量c
print(c)		# 用函数print把变量c的值打印出来

# 自己造一个函数也很简单吧？
