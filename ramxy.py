#!/usr/bin/python
class matrix:
	x=[];
	y=[];
def setMem(matrix):
	n=0;
	for n in range(0,8):
		matrix.x+=[0];
		matrix.y+=[0];
	return matrix;
def report(matrix):
	n=0;
	for n in range(0,8):
		print(str(matrix.x[n])+"	,"+str(matrix.y[n]));
def wmem(matrix,index,x,y):
	matrix.x[index]=x;
	matrix.y[index]=y;
	return matrix;
print("\033c\033[42;30m\n");
matrix1=matrix();
n=0;
x=0;
y=0;
index=0
setMem(matrix1);
for index in range(0,8):
	matrix1=wmem(matrix1,index,x,y);
	x+=1;
	y+=1;
report(matrix);
