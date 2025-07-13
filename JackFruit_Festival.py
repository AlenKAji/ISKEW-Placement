n,m=map(int,input().split())
l1=list(map(int,input().split()))
l1.sort()
print(sum(l1[n-m:]))
