#!/usr/bin/python
print("\033c\033[42;30m\n");
n=raw_input('enumerate values');
print();
ss=n.split(",");
for nn in range(0,len(ss)):
	print (ss[nn]+"="+str(nn)+";");

