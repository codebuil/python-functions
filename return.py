import random;
import time;
import thread;
from Tkinter import *
import tkMessageBox;
rets=[];
tt=1
#change bord w
maxx=120
winx=500
#change bord h
maxy=120
winy=300
t=1
memory=[0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0];
inverter=0;
xx=[];
yy=[];
root=Tk()
sbitmaps=Canvas(root,bg="green",height=winy,width=winx)
def getxy(winx,winy):
	global xx;
	global yy;
	n=0;
	nx=winx
	ny=winy
	while nx >0:
		xx=xx+[nx];
		yy=yy+[ny];
		ny=int(ny*14/16);
		nx=int(nx*14/16);
		if ny<16 or nx<16:
			ny=0;
			nx=0;
	return len(xx);
def getn(maxs):
	return random.randrange(0,maxs,1)
def centers(ww,b):
	return (ww/2)-(b/2)
def changeRoomColor(n,mm):
	global rets;
	global memory;
	colors="";
	if mm==0 and memory[n]==0:
		colors="black";		
	if mm==0 and memory[n]==1:
		colors="green";
	if mm==1 and memory[n]==0:		
		colors="green";		
	if mm==1 and memory[n]==1:
			colors="black";
	sbitmaps.itemconfig(rets[n],fill=colors)	
def movess():
	global inverter;
	inverter=inverter+1;
	if inverter>1:
		inverter=0;
def creatRoom(winx,winy,n):
		global rets;
		global xx;
		global yy;
		colors="";
		if memory[n]==0:		
			colors="black";		
		else:
			colors="green";
		rets=rets+[sbitmaps.create_rectangle(centers(winx,xx[n]),centers(winy,yy[n]),centers(winx,xx[n])+xx[n],centers(winy,yy[n])+yy[n],fill=colors)]
def checkers():
	global t
	global winx;
	global winy;
	global inverter;
	tt=0;
	ll=0;
	n=0;
	nn=0;
	ll=getxy(winx,winy);
	nn=range(0,ll);
	for n in nn:
		creatRoom(winx,winy,n);
	while t >0:
		for n in nn:
			changeRoomColor(n,inverter);
		time.sleep(0.25);
		movess();
		tt=0;
sbitmaps.pack() 
thread.start_new_thread(checkers,());
root.mainloop();
t=0
time.sleep(1)