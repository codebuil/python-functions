#!/usr/bin/python
import random;
def getn(maxs):
	return random.randrange(0,maxs,1);
def getn100(maxs):
	n=0.00;
	n=getn(maxs);
	n=n/100.00;
	return n;
def numbers(n,nnn):
	nn=0
	maxs=50000;
	for nn in range(0,nnn):
		n=n+[getn100(maxs)];
	return n;
def sums(a):
	n=0;
	b=0.00;
	for n in range(0,len(a)):
		b+=a[n];
	return b;
def report(a):
	n=0;
	b=0.00;
	for n in range(0,len(a)):
		b+=a[n];
		print(str(a[n])+"\t\t"+str(b));
	print b;
print("\033c\033[42;30m\n");
nn=[];
n=20;
nn=numbers(nn,n);
print(sums(nn));
print("-----------------------------");
report(nn)