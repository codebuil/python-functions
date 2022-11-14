#!/usr/bin/python

def encoders(number1):
	nn=0;
	ar=[65,66,67,68,69,70];
	nn=len(ar);
	if number1==0:
		return nn;
	nn=ar[number1-1];
	return nn;

	
n=0;
number=0;
print("\033c\033[42;30m\n");
number=encoders(0);
for n in range(0,number):
	print (encoders(n+1));
	