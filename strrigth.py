#!/usr/bin/python
def strrigth(a,b):
	a=a[len(a)-b:len(a)];
	return a;

print("\033c\033[42;30m\n");
aa="01234567890*";
bb="-->"
aa=strrigth(aa,8);
print (aa);