#!/usr/bin/python
matrix=[];
def setMem(matrix):
	n=0;
	for n in range(0,8*8):
		matrix+=[0];
	return matrix;
def report(matrix):
	n=0;
	for n in range(0,8):
		print(matrix[n*8:n*8+8]);
def wmem(matrix,x,y,value):
	matrix[y*8+x]=value;
	return matrix;
print("\033c\033[42;30m\n");
n=0;
x=0;
y=0;
setMem(matrix);
for y in range(0,8):
	for x in range(0,8):
		matrix=wmem(matrix,x,y,int(y*8+x));
report(matrix);