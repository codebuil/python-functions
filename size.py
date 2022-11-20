import thread;
from Tkinter import *
import tkMessageBox;
rets="";
tt=1
#change bord w
maxx=120
#change bord h
maxy=120
t=0
root=Tk()
sbitmaps=Canvas(root,bg="green",height=300,width=500)
def sets(maxx,maxy):
	global rets
	rets=sbitmaps.create_rectangle(0,0,maxx,maxy,fill="white")
def checkers():
    global t
    tt=0;
    sets(maxx,maxy)
    while t > 0:
	tt=0;
sbitmaps.pack() 
thread.start_new_thread(checkers,())
root.mainloop()            
t=0
