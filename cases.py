#!/usr/bin/python
def cases(c,a,b):
	if c==0:
		return a;
	return b;
b=0;
print("\033c\033[42;30m\n");
print ("write 0 or 1:?");
b=input();
print (cases(b,"True","False"));