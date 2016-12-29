from sys import argv

script,filename=argv

print"We're going to erase %r."%filename
print"If you don't want that,hit CTRL-C(^C)."
print"If you want that,hit RETURN."

raw_input("?")

print"Opening the file..."
target=open(filename,'w')

print"Truncating the file.Goodbye!"
target.truncate()

print"Now I'm going to ask you for three lines."

line1=raw_input("line 1:")
line2=raw_input("line 2:")
line3=raw_input("line 3:")

print"I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()

# 写一个和上一个练习类似的脚本，使用 read 和 argv 读取你刚才新建的文件。
# 文件中重复的地方太多了。试着用一个 target.write() 将 line1, line2, line3 打印出来，你可以使用字符串、格式化字符、以及转义字符。
# 找出为什么我们需要给 open 多赋予一个 'w' 参数。提示： open 对于文件的写入操作态度是安全第一，所以你只有特别指定以后，它才会进行写入操作。
