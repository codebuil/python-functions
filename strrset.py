#!/usr/bin/python
def strrigth(a,b):
	dd=len(a);
	bb=dd-b;
	if bb<0:
		bb=0;
	a=a[bb:dd];
	return a;
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
def strrset(a,b):
	dd=len(a);
	ff=len(b);
	if dd<=ff:
		return b;
	aa=b+strrigth(a,dd-ff);
	return aa;


print("\033c\033[42;30m\n");
aa="01234567890";
bb="----"
aa=strrset(aa,bb);
print (aa);