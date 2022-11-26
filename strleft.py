#!/usr/bin/python
def strleft(a,b):
	bb=len(a);
	if b<bb:
		bb=b
	a=a[0:bb];
	return a;

print("\033c\033[42;30m\n");
aa="01234567890*";
bb="-->"
aa=strleft(aa,8);
print (aa);