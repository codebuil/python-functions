import random;
import calendar;
import time;
import thread;
from Tkinter import *
import tkMessageBox;
rets=[];
tt=1
y=0
x=0
t=1
counter=0;
root=Tk()
ss=StringVar()
ss.set(" ")
sbitmaps=Canvas(root,bg="green",height=300,width=500)
def setram():
	y=0
	x=0
	global rets
	for y in range(0,8):
		for x in range(0,8):
			rets=rets+[sbitmaps.create_rectangle(x*20,y*20,x*20+18,y*20+18,fill="white")]
def wram(indexs,value):
	global rets	
	if value==0:
		sbitmaps.itemconfig(rets[indexs],fill="black")
	if value!=0:
		sbitmaps.itemconfig(rets[indexs],fill="white")	
def checkers():
    global t
    global tt
    global rets
    setram()
    counter=0;
    counter2=0;
    while t > 0:
        time.sleep(0.25)
        if counter>len(rets)-1:
            counter=0;
            counter2+=1;
            if counter2>1:
                counter2=0;
        if t==1:
            wram(counter,counter2);
        counter+=1
    tt=0
    print(tt)
    return


sbitmaps.pack() 
thread.start_new_thread(checkers,())
root.mainloop()            
t=0
time.sleep(1)