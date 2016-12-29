 # -- coding: utf-8 -- 
 #函数（function）/方法（method）
 

from sys import argv
script,filename=argv

#函数open
txt=open(filename)

print "Here's your file %r:" % filename
#函数read
print txt.read()
print txt.close()

print"Type the filename again:"
file_again=raw_input(">")

txt_again=open(file_again)
print txt_again.read()
print txt_again.readline()
print txt_again.close()
