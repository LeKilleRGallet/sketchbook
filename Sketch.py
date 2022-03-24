white=0
red=1
green=2
blue=3
yellow=4
orange=5

white_face=[[white,white,white],[white,white,white],[white,white,white]]
red_face=[[red,red,red],[red,red,red],[red,red,red]]
green_face=[[green,green,green],[green,green,green],[green,green,green]]
blue_face=[[blue,blue,blue],[blue,blue,blue],[blue,blue,blue]]
yellow_face=[[yellow,yellow,yellow],[yellow,yellow,yellow],[yellow,yellow,yellow]]
orange_face=[[orange,orange,orange],[orange,orange,orange],[orange,orange,orange]]

mid_face=[red_face,green_face,blue_face,yellow_face]

for i in range(3):
    print('\t', end = '')
    for j in range(3):
        print(white_face[i][j],end=" ")
    print()

print('-'*30)


j = 0
while j < 3:
    i=0
    while i < 4:
        
        for k in range(3):
            print(mid_face[i][j][k],end=" ")
        print('|', end = '')
        i += 1
    print()
    j += 1
print('-'*30)

for i in range(3):
    print('\t', end = '')
    for j in range(3):
        print(orange_face[i][j],end=" ")
    print()