import os
from Tkinter import *

t=1
root=Tk()
root.title("var class object")
root.geometry("500x300")
frame=Frame(root)
frame2=Frame(root)
global ss
ss=StringVar()
ss.set(" ")
iiput=Text(frame2)
iiput2=Entry(frame)
class varNumber:
	names="";
	values=0;
	def gets(v):
		return v.values;
	def sets(v,namess,a):
		v.names=namess
		v.values=a;
	def report(v,abouts):
		iiput.insert(INSERT,v.names+":"+str(v.values)+","+abouts+"\n");
	def add(v,a):
		v.values=v.values+a;
def ups():
	try:
		i=eval(iiput2.get())
	except:
		i=0;
	a=varNumber();
	a.sets("a",10);
	a.report("initial");
	a.add(i);    
	iiput.insert(INSERT,str(a.gets())+"\n");



iiput.width=3
iiput.height=1
iiput2.width=3
iiput2.height=1
frame.pack()
frame.width=500
frame.height=80
frame2.pack(side =BOTTOM)
frame2.width=500
frame2.height=200
sups=Button(frame,text="test",command=ups)
sups.pack(side =LEFT) 
iiput2.pack(side =LEFT) 
iiput.pack(side =BOTTOM) 
root.mainloop()            
t=0
