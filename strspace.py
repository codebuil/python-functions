#!/usr/bin/python
def strstring(a,b,c):
	n=0;
	for n in range(0,c):
		a=a+b;
	return a;
def strspace(a,b):
	return strstring(a," ",b);

print("\033c\033[42;30m\n");
aa="";
bb="-->"
aa=strspace(aa,8);
print (aa+bb);