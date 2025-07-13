n=int(input())
l2=[]
for i in range(n):
    l1=list(map(int,input().split()))
    l2.append(l1)
l2.sort()
l3=[]
l3.append(l2[0])
j=0
for i in range(1,len(l2)):
    if(l3[j][1]<=l2[i][0]):
        l3.append(l2[i])
        j+=1
print(l3)