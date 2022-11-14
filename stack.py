#!/usr/bin/python
def pushs(stacks,value):
	stacks=stacks+[value];
	return stacks;
def pops(stacks1):
	sstacks=[];
	value=-1;
	if len(stacks1)>0:
		value=stacks1[len(stacks1)-1];
		sstacks=stacks1[0:len(stacks1)-1];
		stacks1=sstacks;		
		return value;
	return -1;
stack1=[];
n=0;
number=0;
print("\033c\033[42;30m\n");
number=12;
for n in range(0,number):
	stack1=pushs(stack1,n);
for n in range(0,number):
	print pops(stack1);
