from collections import deque
n=8
k=3
l1=[1,3,-1,-3,5,6,7]
max1=max(l1[:k])
l2=[]
l2.append(max1)
for i in range(k,len(l1)):
    if(max1<l1[i]):
        max1=l1[i]
    l2.append(max1)
print(l2)

    
    


    



