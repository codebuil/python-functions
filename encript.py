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
		try:
			b=ord(c[counter]);
		except:
			print("error on compile!")
		ddd=chr(ord(dd)+b & 255);
		if hh!=0:
			ddd=chr(ord(dd)-b & 255);
		dd=ddd;
		counter+=1;
		counter=resets(counter,ee-1);
		aa+=dd;
	return aa;
codes="";
aa="";
a="";
b="";
c="";
print("\033c\033[42;30m\n");
print("file name:?")
a=raw_input();
print("key:?")
b=raw_input();
print("compile 0:?");
dd=input();
try:
	f= open(a, "r");
	c=f.read();
	f.close();
except:
	print "error load file";
if dd==0:
	aa=add(c,b,0)
else:
	aa=add(c,b,1)
try:
	f= open(a+".out", "w");
	f.write(aa);
	f.close();
except:
	print "error write file";
