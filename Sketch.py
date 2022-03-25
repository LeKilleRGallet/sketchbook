import numpy as np

def tttt(v1,v2,v3,v4):
    return v4, v1, v2,v3


top_face=[[0,'a',0],[0,'b',0],[0,'c',0]]
mid1_face=[[1,'d',1],[1,'e',1],[1,'f',1]]
mid2_face=[[2,'g',2],[2,'h',2],[2,'i',2]]
mid3_face=[[3,'j',3],[3,'k',3],[3,'l',3]]
mid4_face=[[4,'m',4],[4,'n',4],[4,'o',4]]
bottom_face=[[5,'p',5],[5,'q',5],[5,'s',5]]

tempmtrx1=np.array(mid2_face)
tempmtrx2=np.array(mid4_face)

top_face[2],a,bottom_face[0],b=tttt(top_face[2],list(tempmtrx1.T[0]),bottom_face[0],list(tempmtrx2.T[2]))

print(top_face[2],a,bottom_face[0],b)

for _ in range(3):
    mid2_face[_][0]=a[_]

print(mid2_face)





