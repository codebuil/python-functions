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
for y in range(0,10):
	for x in range(0,10):
		rets=rets+[sbitmaps.create_rectangle(x*20,y*20,x*20+10,y*20+10,fill="black")]


def checkers():
    while t > 0:
        time.sleep(1)
    print "exit timer"
    return 


sbitmaps.pack() 
thread.start_new_thread(checkers,())
root.mainloop()            
t=0
print "exit program"    
