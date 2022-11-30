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
root=Tk()
sbitmaps=Canvas(root,bg="green",height=winy,width=winx)
def getn(maxs):
	return random.randrange(0,maxs,1)
def centers(ww,b):
	return (ww/2)-(b/2)
def sets(winx,winy):
	global rets
	n=0;
	nx=winx
	ny=winy
	cc=0;
	while nx >0:
		if cc==0:		
			rets=rets+[sbitmaps.create_rectangle(centers(winx,nx),centers(winy,ny),centers(winx,nx)+nx,centers(winy,ny)+ny,fill="green")]
		else:		
			rets=rets+[sbitmaps.create_rectangle(centers(winx,nx),centers(winy,ny),centers(winx,nx)+nx,centers(winy,ny)+ny,fill="black")]		
		cc=cc+1;
		if cc>1:
			cc=0;
		ny=int(ny*14/16);
		nx=int(nx*14/16);
		if ny<16 or nx<16:
			ny=0;
			nx=0;
def checkers():
    global t
    tt=0;
    sets(winx,winy)
    while t >0:
        tt=0;
sbitmaps.pack() 
thread.start_new_thread(checkers,())
root.mainloop()            
t=0
time.sleep(1)