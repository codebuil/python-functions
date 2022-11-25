#!/usr/bin/python
def strmid(a,b,c):
	a=a[b:c];
	return a;
print("\033c\033[42;30m\n");
aa="hi , hello world";
print(aa);
aa=strmid(aa,2,8);
print (aa);