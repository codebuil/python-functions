import random;
import time;
import thread;
from Tkinter import *
import tkMessageBox;
rets=[];
tt=1
#change bord w
maxx=0
winx=500
#change bord h
maxy=0
winy=300
t=1
inverter=1;
inverter2=1;
xx=[];
yy=[];
root=Tk()
steeps=5;
sbitmaps=Canvas(root,bg="green",height=winy,width=winx)
def refreshRoad():
	global maxx;
	global maxy;
	global xx;
	global yy;
	sbitmaps.coords(rets[0],xx[0]+maxx,yy[0],xx[1]+maxx,yy[1]+maxy);
	sbitmaps.coords(rets[1],xx[2]+maxx,yy[2]+maxy,xx[3]+maxx,yy[3]);
def movess():
	global maxx;
	global maxy;
	global inverter;
	maxx=maxx+(inverter*steeps);
def movess2():
	global maxx;
	global maxy;
	global inverter2;
	maxy=maxy+(inverter2*steeps);
def inverte():
	global inverter;
	if inverter==-1:
		inverter=1;
	else:
		inverter=-1;
def inverte2():
	global inverter2;
	if inverter2==-1:
		inverter2=1;
	else:
		inverter2=-1;

def defs():
	global xx;
	global yy;
	global maxy;
	global maxx;
	maxy=0;
	maxx=0;
	xx=xx+[0];
	yy=yy+[winy];
	xx=xx+[winx/2];
	yy=yy+[0];
	xx=xx+[winx/2];
	yy=yy+[0];
	xx=xx+[winx];
	yy=yy+[winy];
def createRoad():
	global rets;
	colors="black";
	rets=rets+[sbitmaps.create_line(xx[0],yy[0],xx[1],yy[1],fill=colors)];
	rets=rets+[sbitmaps.create_line(xx[2],yy[2],xx[3],yy[3],fill=colors)];
def checkers():
	global t
	global winx;
	global winy;
	global inverter;
	tt=0;
	ll=0;
	n=0;
	nn=0;
	createRoad();
	while t >0:
		refreshRoad();
		if maxy>winy/2:
			inverte2()
		if maxy<0:
			inverte2()
		if maxx>winx/2:
			inverte()
		if maxx<-(winx/2):
			inverte()
		time.sleep(1)
		movess();
		movess2();
		tt=0;
defs();
sbitmaps.pack() 
thread.start_new_thread(checkers,());
root.mainloop();
t=0
time.sleep(1)