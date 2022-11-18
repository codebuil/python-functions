toInc=0;
def inc():
    global toInc;
    toInc=toInc+1;
print("\033c\033[42;30m\n");
for a in range(0,10):
	inc();
print(toInc);
