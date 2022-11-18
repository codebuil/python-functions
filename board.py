import random;
import calendar;
import time;
import thread;
from Tkinter import *
import tkMessageBox;
rets=[];
y=0
x=0
t=1
root=Tk()
ss=StringVar()
ss.set(" ")
sbitmaps=Canvas(root,bg="green",height=300,width=500)
for y in range(0,8):
	for x in range(0,8):
		rets=rets+[sbitmaps.create_rectangle(x*20,y*20,x*20+18,y*20+18,fill="white")]


def checkers():
    while t > 0:
        time.sleep(1)
    return 


sbitmaps.pack() 
thread.start_new_thread(checkers,())
root.mainloop()            
t=0

