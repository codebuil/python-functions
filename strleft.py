#!/usr/bin/python
def strleft(a,b):
	a=a[0:b];
	return a;

print("\033c\033[42;30m\n");
aa="01234567890*";
bb="-->"
aa=strleft(aa,8);
print (aa);