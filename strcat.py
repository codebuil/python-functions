#!/usr/bin/python
def strcat(a,b):
	a=a+b;
	return a;
print("\033c\033[42;30m\n");
aa="hi , ";
bb="hello world";
aa=strcat(aa,bb);
print (aa);