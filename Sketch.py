import time

def loading():

    print('\n')
    for _ in range(0, 100):

        if _%4 == 0:
            a = '/'
        elif _%4 == 1:
            a = '—'
        elif _%4 == 2:
            a = '\\'
        else:
            a = '|'
        
        print('\tloading ' + a, end='\r')
        time.sleep(1/10)

loading()