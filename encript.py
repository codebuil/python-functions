#!/usr/bin/python
def resets(a,b):
	if a<b:
		return a
	return 0;
def add(a,c,hh):
	b=0;
	dd="";
	aa="";
	n=0;
	bb=len(a);
	ee=len(c);
	cc=range(0,bb);
	counter=0;
	ddd="";	
	for n in cc:
		dd=a[n];
		b=ord(c[counter]);
		ddd=chr(ord(dd)+b & 255);
		if hh!=0:
			ddd=chr(ord(dd)-b & 255);
		dd=ddd;
		counter+=1;
		counter=resets(counter,ee-1);
		aa+=dd;
	return aa;
codes="key!";
print("\033c\033[42;30m\n");
aa=add("hello world",codes,0)
print (aa);
print (add(aa,codes,1));