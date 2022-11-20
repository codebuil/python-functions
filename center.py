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
t=0
root=Tk()
sbitmaps=Canvas(root,bg="green",height=300,width=500)
def centers(ww,b):
	return (ww/2)-(b/2)
def sets(winx,winy,maxx,maxy):
	global rets
	xx=centers(winx,maxx)
	yy=centers(winy,maxy)
	rets=sbitmaps.create_rectangle(xx,yy,xx+maxx,yy+maxy,fill="white")
def checkers():
    global t
    tt=0;
    sets(winx,winy,maxx,maxy)
    while t > 0:
	tt=0;
sbitmaps.pack() 
thread.start_new_thread(checkers,())
root.mainloop()            
t=0
