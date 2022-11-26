#!/usr/bin/python
class movess:
	dates="";
	ref="";
	ref2="";
	amount=0.00;
mmoves=[];	
def menutrans():
	global mmoves;
	print("data: ?");
	d=raw_input();
	print("ref: ?");
	r1=raw_input();	
	print("ref2: ?");
	r2=raw_input();	
	print("value: ?");
	am=input();	
	mmoves=mmoves+[movess()];
	poss=len(mmoves)-1;
	mmoves[poss].dates=d;
	mmoves[poss].ref=r1;
	mmoves[poss].ref2=r2;
	mmoves[poss].amount=am;
def reportss(rp,tt,r0):
	ttt=0.00;
	if r0==0:
		ttt=tt+rp.amount;
	else:
		ttt=tt-rp.amount;
	print (rp.dates+","+rp.ref+","+rp.ref2+","+str(rp.amount)+"_="+str(ttt));
	return ttt;
def reports(rp):
	print (rp.dates+","+rp.ref+","+rp.ref2+","+str(rp.amount));
def menuall():
	print("list all");
	global mmoves;
	vv=0;
	n=0;
	le=len(mmoves);
	for n in range(0,le):
		reports(mmoves[n]);
def menuclient():
	print("list client ref?:");
	i=raw_input()
	global mmoves;
	vv=0;
	n=0;
	le=len(mmoves);
	for n in range(0,le):
		if mmoves[n].ref==i:
			vv=reportss(mmoves[n],vv,1);
		if mmoves[n].ref2==i:
			vv=reportss(mmoves[n],vv,0);

def mainmenu():
	whi=-1;
	while whi!=3:
		print("0-make transaction");
		print("1-list all transactions");
		print("2-list client");
		print("3-exit");
		whi=input();
		if whi==0:
			menutrans();
		if whi==1:
			menuall();
		if whi==2:
			menuclient();
print("\033c\033[42;30m\n");
mainmenu();