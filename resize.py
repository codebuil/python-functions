import random;
import time;
import thread;
from Tkinter import *
import tkMessageBox;
rets="";
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
def sets(winx,winy,maxx,maxy):
	global rets
	xx=centers(winx,maxx)
	yy=centers(winy,maxy)
	rets=sbitmaps.create_rectangle(xx,yy,xx+maxx,yy+maxy,fill="white")
def resizes(winx,winy,maxx,maxy):
	print("x : " +str(winx)+" Y : "+str(winx))
	sbitmaps.coords(rets,centers(winx,maxx),centers(winy,maxy),centers(winx,maxx)+winx,centers(winy,maxy)+winy)
def checkers():
    global t
    tt=0;
    sets(winx,winy,maxx,maxy)
    print "xxx."
    while t > 0:
	time.sleep(0.24)
	resizes(winx,winy,getn(winx),getn(winy))
sbitmaps.pack() 
thread.start_new_thread(checkers,())
root.mainloop()            
t=0
time.sleep(1)