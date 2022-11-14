#!/usr/bin/python

def score(number1,number2):
	nn=number1;
	nn=nn+number2;
	return nn;
	
n=0;
number=0;
print("\033c\033[42;30m\n");
for n in range(0,32):
	number=score(number,100);
	print (number);