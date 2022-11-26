#!/usr/bin/python
def strleft(a,b):
	bb=len(a);
	if b<bb:
		bb=b
	a=a[0:bb];
	return a;
def strstring(a,b,c):
	n=0;
	for n in range(0,c):
		a=a+b;
	return a;
def strspace(a,b):
	return strstring(a," ",b);
def strlset(a,b):
	dd=len(a);
	ff=len(b);
	if dd<=ff:
		return b;
	aa=strleft(a,dd-ff)+b;
	return aa;


print("\033c\033[42;30m\n");
aa="01234567890";
bb="----"
aa=strlset(aa,bb);
print (aa);