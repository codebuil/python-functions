#!/usr/bin/python
class movess:
	dates="";
	ref="";
	ref2="";
	amount=0.00;
sizes11="";
sizes16="";
mmoves=[];	
fileToOpen="moves.cvs";
winsep="\r\n";
macsep="\r";
lunixsep="\n";
seps=lunixsep;
def strstring(a,b,c):
	n=0;
	for n in range(0,c):
		a=a+b;
	return a;
def strspace(a,b):
	return strstring(a," ",b);
def strleft(a,b):
	bb=len(a);
	if b<bb:
		bb=b
	a=a[0:bb];
	return a;
def strlset(a,b):
	dd=len(a);
	ff=len(b);
	if dd<=ff:
		return b;
	aa=strleft(a,dd-ff)+b;
	return aa;
def definess():
	global sizes11;
	global sizes16;
	sizes11=strspace("",11);
	sizes16=strspace("",16);
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
	print (strlset(sizes16,rp.dates)+"|"+strlset(sizes11,rp.ref)+"|"+strlset(sizes11,rp.ref2)+"|"+strlset(sizes11,str(rp.amount))+"|"+strlset(sizes11,str(ttt)));
	return ttt;
def freports(files,n):
	global mmoves;
	files.write(mmoves[n].dates+","+mmoves[n].ref+","+mmoves[n].ref2+","+str(mmoves[n].amount)+"\n");
def saves():
	global mmoves;
	ii=0;
	i=len(mmoves);
	n=0;
	try:
		f= open(fileToOpen, "w+");
		if i>0:
			for n in range(0,i):
				freports(f,n);
	except:
		ii=0;
	f.close();
def collstrans(nn):
	global mmoves;
	poss=0;	
	mmoves=mmoves+[movess()];
	poss=len(mmoves)-1;
	ii=0;	
	ii=len(nn);
	if ii>3:
		mmoves[poss].dates=nn[0];
		mmoves[poss].ref=nn[1];
		mmoves[poss].ref2=nn[2];
		mmoves[poss].amount=eval(nn[3]);

def colls(nn):
	n=0;
	ii=0;
	nnn=nn.split(",");
	ii=len(nnn);
	if ii>3:
		collstrans(nnn);
	
def lfile():
	global mmoves;
	mmoves=[];
	rvalue=[];
	rrvalue="";
	ii=0;
	n=0;
	try:
		f= open(fileToOpen, "r");
		rrvalue=f.read();
		f.close();
		rvalue=rrvalue.split(seps);
	except:
		ii=0;
	ii=len(rvalue);
	if ii>0:
		for n in range(0,ii):
			colls(rvalue[n]);
def loads():
	global mmoves;
	mmoves=[];	
	lfile();
def reports(rp):
	print (strlset(sizes16,rp.dates)+"|"+strlset(sizes11,rp.ref)+"|"+strlset(sizes11,rp.ref2)+"|"+strlset(sizes11,str(rp.amount)));
def menuall():
	print("list all");
	global mmoves;
	vv=0;
	n=0;
	le=len(mmoves);
	print(strstring("","-",80));
	for n in range(0,le):
		reports(mmoves[n]);
	print(strstring("","-",80));
def menuclient():
	print("list client ref?:");
	i=raw_input()
	global mmoves;
	vv=0;
	n=0;
	le=len(mmoves);
	print(strstring("","-",80));
	for n in range(0,le):
		if mmoves[n].ref==i:
			vv=reportss(mmoves[n],vv,1);
		if mmoves[n].ref2==i:
			vv=reportss(mmoves[n],vv,0);
	print(strstring("","-",80));
def changename():
	try:
		print("file cvs name")
		i=raw_input()
		fileToOpen=i;
	except:
		fileToOpen="moves.cvs";
def mainmenu():
	whi=-1;
	while whi!=6:
		print("0-make transaction");
		print("1-list all transactions");
		print("2-list client");
		print("3-save to cvs");	
		print("4-load from cvs");	
		print("5-change cvs name");	
		print("6-exit");
		whi=input();
		if whi==0:
			menutrans();
		if whi==1:
			menuall();
		if whi==2:
			menuclient();
		if whi==3:
			saves();
		if whi==4:
			loads();
		if whi==5:
			changename();
print("\033c\033[42;30m\n");
definess();
mainmenu();