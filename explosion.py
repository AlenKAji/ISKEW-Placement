n,a,b=map(int,input().split())
l1=[]
l2=[]
dir=[(1,0),(0,1),(-1,0),(0,-1)]
for i in range(n):
    l1=list(map(int,input().split()))
    l2.append(l1)
queue=[]
visited=set()
queue.append([a,b])
while(queue):
    x,y=queue.pop()
    for dx,dy in dir:
        dirx=x+dx
        diry=y+dy
        if([dirx,diry] in visited):
            continue
        visited.add([dirx,diry])


    