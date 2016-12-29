 # -- coding: utf-8 -- 
 #创建一个新函数： def 函数名（参数）:
 #函数（function）
 #解包(unpack):把 argv 中的东西解包，将所有的参数依次赋予左边的变量名。
 #print后跟括号（）
 
#函数解包过程 
def print_two(*args):
     arg1,arg2=args
     print "arg1:%r,arg2:%r"%(arg1,arg2)

print_two("Zed","Shaw")

#函数可以跳过解包过程
def print_two_again(arg1,arg2):
    print"arg1:%r,arg2:%r"%(arg1,arg2)
print_two_again("Zed","Shaw")

#函数可以接受单个参数
def print_one(arg1):
    print"arg1:%r"%arg1
print print_one("First")

#函数可以不接受任何参数
def print_one():
    print"I got nothin'."
print_one()
