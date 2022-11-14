#!/usr/bin/python
def max(numb1,numb2):
	if numb1 > numb2:
		return numb1;
	return numb2;
	
n=0;
print("\033c\033[42;30m\n");
for n in range(0,20):
	print (max(10,n));