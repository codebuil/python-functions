#!/usr/bin/python
getInt=5;
setInt=4;
divs=3;
mult=2;
subs=1;
adds=0
x=0;
xx=16;
xxx=0;
readss=0;
def floatEmulator(a,b,matfunc):
	ii=0;
	precs=1000;
	if matfunc==0:
		ii=a+b;
	if matfunc==1:
		ii=a-b;
	if matfunc==2:
		ii=a*b;
	if matfunc==3:
		ii=a/b;
	if matfunc==4:
		ii=a*precs;
	if matfunc==5:
		ii=a/precs;
	return ii;
nn=0
print("\033c\033[42;30m\n");
print (floatEmulator(10,10,adds));
print (floatEmulator(20,10,subs));
print (floatEmulator(20,10,mult));
print (floatEmulator(20,10,divs));
print (floatEmulator(20,0,setInt));
print (floatEmulator(2000,0,getInt));