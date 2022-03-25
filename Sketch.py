


top_face=[[0,0,0],[0,0,0],[0,0,0]]
mid1_face=[[1,1,1],[1,1,1],[1,1,1]]
mid2_face=[[2,2,2],[2,2,2],[2,2,2]]
mid3_face=[[3,3,3],[3,3,3],[3,3,3]]
mid4_face=[[4,4,4],[4,4,4],[4,4,4]]
bottom_face=[[5,5,5],[5,5,5],[5,5,5]]


print(mid1_face)
print(mid2_face)
print(mid3_face)
print(mid4_face)

temp2=mid1_face[0]

temp1=temp2
temp2=mid2_face[0]
mid2_face[0]=temp1

temp1=temp2
temp2=mid3_face[0]
mid3_face[0]=temp1

temp1=temp2
temp2=mid4_face[0]
mid4_face[0]=temp1

temp1=temp2
temp2=mid1_face[0]
mid1_face[0]=temp1

print()

print(mid1_face)
print(mid2_face)
print(mid3_face)
print(mid4_face)




