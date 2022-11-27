#!/usr/bin/python
def enumorator(a,b):
	if a<len(b) and a>-1:
		return b[a];
	return b[len(b)-1];
b=0;
c=["X86","X186","X286","X386","x486"];
print("\033c\033[42;30m\n");
print ("write 0 or 4:?");
b=input();
print (enumorator(b,c));