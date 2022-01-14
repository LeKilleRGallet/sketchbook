import random
import numpy as np

sudoku_size = 9
difficulty_level = 1

# def random_matrix(difficulty, sudoku_size):
c = [10*difficulty_level]+[1]*sudoku_size
#     m = []
#     total_zeros = 0
#     for _ in range(sudoku_size):
#         m.append(random.sample([0, *range(1,sudoku_size+1)], counts = c, k = sudoku_size))
#         total_zeros +=m[_].count(0)

#     m = np.array(m)
#     print(m)
#     print(total_zeros)
#     print(total_zeros/(sudoku_size*sudoku_size))
    


# random_matrix(2, 9)





obj = {'ls{}'.format(i):random.sample([0, *range(1,sudoku_size+1)], counts = c, k = sudoku_size) for i in range(1,sudoku_size+1)}

print(obj['ls1'])
print(obj['ls1'].count(0))
print(obj)