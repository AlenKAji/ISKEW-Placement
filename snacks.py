n=6 
k=3
l1=[4,-1,2,1,-6,17]
sum1=sum(l1[:k])
maxsum=sum1
maxsum2=-20
for i in range(0,len(l1)-k):
    temp=maxsum2
    sum1=l1[k+i]+sum1-l1[i]
    if(maxsum<sum1):
        maxsum2=maxsum
        maxsum=sum1
    if(maxsum2==maxsum):
        maxsum2=temp

    
print(maxsum, maxsum2)
