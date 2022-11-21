#!/usr/bin/python
import time;
def report(t):
	local=time.asctime(time.localtime(t));
	print (local);
def add(a,b):
	return a+b;
print("\033c\033[42;30m\n");
t=time.time();
report(t)
tt=t+12;
report(tt);
print("waiting for future event");
while t<tt:
	t=time.time();
#print add(10,10);