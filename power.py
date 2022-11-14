#!/usr/bin/python
def power(numb1,numb2):
	n=0;
	nn=numb1;
	if numb2==0:
		return 1;
	if numb2==1:
		return numb1;
	for n in range(0,numb2-1):
		nn=nn*numb1;
	return nn;
	
n=0;
print("\033c\033[42;30m\n");
for n in range(0,32):
	print (power(2,n));