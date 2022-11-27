#!/usr/bin/python
def enumorator(a,b):
	if a<len(b) and a>-1:
		return b[a];
	return b[len(b)-1];
def definess(value,chars,seps):
	n=0;
	i=0;
	try:
		i=value.index(chars);
	except:
		i=-1;
	if i>-1:
		print(value);
	else:
		print(seps+value);
def printL(lists):
	n=0;
	nn=len(lists);
	nnn=range(0,nn);
	for n in nnn:
		definess(enumorator(n,lists),"+","\t");

b=0;
c=["+arm","arm4","arm5","arm6","arm7","arm8","+x86","x8086","x80186","x80286","x80386","x80486"];
print("\033c\033[42;30m\n");
printL(c);