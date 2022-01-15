import numpy as np
import random

# grid=[random.sample([0,1,2,3,4,5,6,7,8,9], counts = [10,1,1,1,1,1,1,1,1,1], k=9)  for i in range(9)]



# print(exx)
# print(exx[0,:])
# print(exx[:,0])

# llal=[*range(1,9+1)]
# # random.shuffle(llal)

# print(llal)
# print(len(exx))
# print(len(exx)*len(exx))

# for i in range(81):
#     row = i//9
#     col = i%9
#     print('i={}'.format(i), 'row={}'.format(row), 'col={}'.format(col))

# print(np.array(grid))

# number_list=[*range(1,len(grid)+1)]

# print('//')
# print(number_list)
# print('//')
# for i in range(len(grid)*len(grid)):
#     row = i//len(grid)
#     col = i%len(grid)
#     random.shuffle(number_list)
#     l_col = [l_row[col] for l_row in grid] #list of column values
#     print('//')
#     print(l_col)
#     for num in number_list:
#         if not num in grid[row]:
# #             pass
# subgrid_size=3

# class Found(Exception):
#     pass
# # for i in range(0,81):

# i=random.randint(0,80)
# row=i//9
# col=i%9
# try:
#     for subrow in range(1,subgrid_size+1):
#         for subcol in range(1,subgrid_size+1):
#             if row<(subgrid_size*subrow) and col<(subgrid_size*subcol):
#                 print('i={}'.format(i), 'row={}'.format(row), 'col={}'.format(col), 'subrow={}'.format(subrow), 'subcol={}'.format(subcol), 'subgrid_size={}'.format(subgrid_size))
#                 subgrid=[grid[j][subgrid_size*(subcol-1):subgrid_size*subcol] for j in range(subgrid_size*(subrow-1),subgrid_size*subrow)]
#                 raise Found
# except Found:
#     print(np.array(subgrid))

l = [[0,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,16,17,18,19]]

# result=any(1 in _ for _ in l)

# print(result)
ss=[]

for sublist in l:
    print(sublist)
    for element in sublist:
        ss.append(element)
        print(ss)