#!/usr/bin/python
def strmid(a,b,c):
	dd=len(a);
	bb=b;
	cc=c;
	if bb<0:
		bb=0;
	if cc<0:
		cc=0;
	if bb>dd:
		bb=dd;
	if cc>dd:
		cc=dd;
	a=a[bb:cc];
	return a;
print("\033c\033[42;30m\n");
aa="hi , hello world";
print(aa);
aa=strmid(aa,2,8);
print (aa);