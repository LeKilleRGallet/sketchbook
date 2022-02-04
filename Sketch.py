import random


a=random.randint(0,100)

n_1=0
n_2 = int(a*(1/5))
n_3 = int(a*(2/5))
n_4 = int(a*(3/5))
n_5 = int(a*(4/5))
n_6 = int(a*(5/5))


print(n_1,n_2,n_3,n_4,n_5,n_6)

rndnum_1=random.randint(n_1,n_2)
rndnum_2=random.randint(n_2,n_3)
rndnum_3=random.randint(n_3,n_4)
rndnum_4=random.randint(n_4,n_5)
rndnum_5=random.randint(n_5,n_6)

print(rndnum_1,rndnum_2,rndnum_3,rndnum_4,rndnum_5)

print(a)