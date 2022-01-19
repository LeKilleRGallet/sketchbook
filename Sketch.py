n = int(input())

def padovan(num):
    padovan_prev = 0
    padovan_secprev = 0
    padovan_thirprev = 0
    for i in range(num+1):
        if i == 0:
            padovan = 1
        elif i == 1:
            padovan = 1
        elif i == 2:
            padovan = 1
        else:
            padovan = padovan_thirprev + padovan_secprev
        padovan_thirprev = padovan_secprev
        padovan_secprev = padovan_prev
        padovan_prev = padovan
        

    return padovan
    

n = padovan(n)

print(n)