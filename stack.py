#!/usr/bin/python
stack1=[];
def pushs(stacks,value):
	stacks=stacks+[value];
	return stacks;
def pops():
	global stack1;	
	sstacks=[];
	value=-1;
	if len(stack1)>0:
		value=stack1[len(stack1)-1];
		sstacks=stack1[0:len(stack1)-1];
		stack1=sstacks;		
		return value;
	return -1;
n=0;
number=0;
print("\033c\033[42;30m\n");
number=12;
for n in range(0,number):
	stack1=pushs(stack1,n);
for n in range(0,number):
	print pops();