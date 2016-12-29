# -- coding: utf-8 -- 
#modules模组  libraries库 argv参数 unpack解包
#执行命令 python ex13.py argv1 argv2 argv3

from sys import argv

a,b,c,d= argv

print "The script is called:", a
print "Your first variable is:", b
print "Your second variable is:", c
print "Your third variable is:", d

# 在终端运行会遇到问题，解决方法详见： https://www.zhihu.com/question/19932406
# 将 raw_input 和 argv 一起使用，让你的脚本从用户手上得到更多的输入。
