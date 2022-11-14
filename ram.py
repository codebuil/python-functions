#!/usr/bin/python
def setram(ramr):
	n=0;
	for n in range(0,12):
		ramr=ramr+[n];
	return ramr;
def ram(indexs):
	if indexs==0:
		return len(ramr);
	return ramr[indexs-1];
ramr=[];
n=0;
number=0;
ramr=setram(ramr);
print("\033c\033[42;30m\n");
number=ram(0);
for n in range(0,number):
	print ram(n+1);