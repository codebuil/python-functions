#!/usr/bin/python
class varNumber:
	names="";
	values=0;
	def gets(v):
		return v.values;
	def sets(v,namess,a):
		v.names=namess
		v.values=a;
	def report(v,abouts):
		print(v.names+":"+str(v.values)+","+abouts);
	def add(v,a):
		v.values=v.values+a;
print("\033c\033[42;30m\n");
a=varNumber();
a.sets("a",10);
a.report("initial");
a.add(10);
print(a.gets());
