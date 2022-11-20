import random;
import calendar;
import time;
import thread;
from Tkinter import *
import tkMessageBox;

t=1
root=Tk()
sbitmaps=Canvas(root,bg="green",height=300,width=500)
ball=sbitmaps.create_oval(0,0,20,20,fill="black")
cursors=sbitmaps.create_rectangle(230,250,270,270,fill="white")

def checkers():
    x=0
    y=0
    xt=8
    yt=8
    varx=250
    global t;
    root.title("pong")            
    while t > 0:
        x=x+xt
        y=y+yt
        if x > 480:
            xt=-8
        if y > 280:
            yt=-8
        if x < 9:
            xt=8
        if y < 9:
            yt=8
	if y> 240:
            t=0;
            root.title("game over")
	varx=x
	if varx>x-20 and varx<x+20 and y<250 and y>230:
            t=1;
            yt=-8;
	sbitmaps.coords(cursors,varx-20,250,varx+20,270)
        sbitmaps.move(ball,xt,yt)
        time.sleep(0.1)
    print "exit timer"
    return 


sbitmaps.pack() 
thread.start_new_thread(checkers,())
root.mainloop()            
t=0
time.sleep(3)
print "exit program"    
