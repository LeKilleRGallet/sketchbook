import time
import os

def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system("cls")

def loading():

    clear()
    print()
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
    clear()

# loading()

a=[[1,2,3,4,5,6,7,8,9,10],[15,16,17,18,19,20,21,22,23,24]]

a_id=[[],[]]

for i in range(len(a)):
    for j in range(len(a[i])):
        print(f'a[{i}][{j}] id is {id(a[i][j])}')
        a_id[i].append(id(a[i][j]))

print(a_id)

    