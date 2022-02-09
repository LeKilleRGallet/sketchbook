import time

def loading():
    for i in range(30):
        if i%4==0:
            r='/'
        elif i%4==1:
            r='—'
        elif i%4==2:
            r='\\'
        elif i%4==3:
            r='|'
        print('loading...' + r,end='\r')
        time.sleep(0.1)

loading()
