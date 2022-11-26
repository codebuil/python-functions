#!/usr/bin/python
def add(a,b):
	dd="";
	aa="";
	n=0;
	bb=len(a);
	cc=range(0,bb);
	for n in cc:
		dd=a[n];
		dd=chr(ord(dd)+b);
		aa+=dd;
	return aa;
codes=10;
print("\033c\033[42;30m\n");
aa=add("hello world",codes)
print (aa);
print (add(aa,-codes));