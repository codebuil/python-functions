#!/usr/bin/python
def inverter(numb1,maxs):
	return maxs-numb1;
	
n=0;
print("\033c\033[42;30m\n");
for n in range(0,20):
	print (inverter(n,20));