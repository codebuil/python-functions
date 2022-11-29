#!/usr/bin/python
class pulse:
	value=0;
	def jks(jkk):
		if jkk.value==0:
			jkk.value=1;
		else:
			jkk.value=0;
		return jkk.value;
jkj=pulse();
n=0;
print("\033c\033[42;30m\n");
for n in range(0,10):
	print(jkj.jks());