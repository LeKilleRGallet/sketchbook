import random


prob=0.5
arr1=[0,1]
weights=[1-prob,prob]
sum_a=0
for _ in range(3):
    a=random.choices(arr1,weights,k=1)
    sum_a+=a[0]
print(sum_a)


