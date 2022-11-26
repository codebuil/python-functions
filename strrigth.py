#!/usr/bin/python
def strrigth(a,b):
	dd=len(a);
	bb=dd-b;
	if bb<0:
		bb=0;
	a=a[bb:dd];
	return a;

print("\033c\033[42;30m\n");
aa="01234567890*";
bb="-->"
aa=strrigth(aa,8);
print (aa);