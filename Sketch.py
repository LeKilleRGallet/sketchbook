# # # # # # while True:
# # # # # #     try:
# # # # # #         range_min = input('insert floor: ')
# # # # # #         if range_min == '':
# # # # # #             range_min = None
# # # # # #             break
# # # # # #         else:
# # # # # #             range_min = int(range_min)
# # # # # #             break
# # # # # #     except ValueError:
# # # # # #         print("Invalid input, just integers or empty, please try again")

# # # # # # while True:
# # # # # #     try:
# # # # # #         range_max = input('insert ceil: ')
# # # # # #         if range_max == '':
# # # # # #             range_max = None
# # # # # #             break
# # # # # #         else:
# # # # # #             range_max = int(range_max)
# # # # # #             break
# # # # # #     except ValueError:
# # # # # #         print("Invalid input, just integers or empty, please try again")

# # # # # # print(range_min, range_max)


# # # # # # # a = input('insert floor: ')

# # # # # # # print(a=='')


# # # # # a = 123123**0.5

# # # # # print(a)

# # # # # print(int(a))

# # # # # print(round(a))


# # # # a = 100000000

# # # # print(len(str(a)))

# # # a = 4

# # # b = a**0.5

# # # print(b)

# # # print(type(b))

# # # if type(b) == type(int()):
# # #     print('int')
# # # else:
# # #     print('float')

# # i = 5

# # print(i == int(i**0.5)**2)

# print((13%2, 13%3, 13%5, 13%7) == (1, 1, 3, 6))

# # a, b, c, d = 13%2,3,5,7

# # print(a,b,c,d == 0)

def prime(n, primes):
    if n<=1:
        return True
    elif n in (2,3,5,7):
        return False
    else:
        if 0 in {n%2, n%3, n%5, n%7}:
            return True
        else:
            sqrt_n = n**0.5
            if n == int(sqrt_n)**2:
                return True
            else:
                for i in primes:
                    if i > (int(sqrt_n)+1):
                        return False
                    if n%i == 0:
                        return True



            
#             ### old
#             for i in range(2,int(n**0.5)+1):
#                 # print(i)
#                 if n%i==0:
#                     return True

# a = 13

# print(0 in {a%2, a%3, a%5, a%7})

# a = []

# for i in a:
#     print(i)
def run():
    """
    docstring
    """
    primes = []
    top = int(99194853094755497**0.5)+1 ## 314'952'144.13424065 aprox 22M primes <
    for i in range(1,top):
        if prime(i, primes) != True:
            primes.append(i)
            print(len(primes))
    with open("file.txt", "w") as output:
        output.write(str(primes))
    # print(len(primes))
    # percentage = len(primes)*100/top
    
    # print(f"{percentage}%")


if __name__ == "__main__":
    run()

# print(3 not in range(2,4))

# a = 9
# print(a)
# b = a**0.5
# print(b)
# c=int(b)**2
# print(c)
# print(c == a)

# a = []

# print(a[-1])

# def aaaa(a):
#     while True:
#         if a > 1:
#             return True
#         else:
#             return False

# print(aaaa(2))


# while True:
#     for i in range(1,10):
#         if i == 7:
#             print(i)
#             break
#         else:
#             print(f'{i} is not 7')
#     print('in while')
    

# a = 7

# print(list(range(a,a**2)))