 # -- coding: utf-8 -- 
#待续

from sys import argv
from os.path import exists

script,from_file,to_file=argv

print"Copying from %s to %s"%(from_file, to_file)

#
input=open(from_file)
indata=input.read()

print"The input file is %d bytes long"%len(indata)

print"Dose the output file exist?%r"%exists(to_file)
print"Ready,hit ENTER to continue,CTRL-C to abort."
raw_input()
