#!/usr/bin/python
def setram(ramr):
	n=0;
	for n in range(0,12):
		ramr=ramr+[0];
	return ramr;
def wram(ramr,indexs,value):
	ramr[indexs]=value;
def ram(ramr,indexs):
	if indexs==0:
		return len(ramr);
	return ramr[indexs-1];
ramr=[];
n=0;
number=0;
ramr=setram(ramr);
print("\033c\033[42;30m\n");
number=ram(ramr,0);
for n in range(0,number):
	wram(ramr,n,n);
for n in range(0,number):
	print ram(ramr,n+1);