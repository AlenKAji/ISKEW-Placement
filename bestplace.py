n=int(input())
sumx=0
sumy=0
for i in range(n):
    x,y=map(int,input().split())
    sumx+=x
    sumy+=y
print(str(sumx//n)+" "+str(sumy//n))