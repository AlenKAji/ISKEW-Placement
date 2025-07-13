n,a,b=map(int,input().split())
l1=[]
l2=[]
for i in range(n):
    l1=list(map(int,input().split()))
    l1.append(i+1)
    l2.append(l1)
l2.sort(key=lambda x:(abs(x[0]-a)+abs(x[1]-b),x[2]))
for i in range(n):
    print(l2[i][-1],end=" ")
