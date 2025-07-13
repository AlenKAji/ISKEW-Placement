#first n prime_no.s
"""n=int(input("Enter No."))
l1=[]
for i in range(2,n):
    count=0
    for j in range(2,i//2+1):
        if(i%j==0):
            count+=1
    if(count==0):
        l1.append(i)
print(l1)
"""
n=int(input("Enter No."))
"""composite=[]
prime=[0]*n+1]
for i in range(2,n):
    for j in range(2*i,n,i):
        prime[j]=1
for i in range(2,len(prime)):
    if(prime[i]==0):
        print(i,end=", ")  """  
if n > 2:
    print(2, end=", ")
prime=[0]*((n//2)-1)
for i in range(3,n//2,2):
    if(prime[i//2-1]==0):
        for j in range(i*i,n,i*2):
            if(j%2!=0):
                prime[j//2-1]=1
for i in range(len(prime)):
    if(prime[i]==0):
        print((i+1)*2+1,end=", ")

"""a=eval(input("Enter the limit:"))
primes=[]
s=((a-3)//2)+1
isprime=[True]*s    
def m(a,s):
    p=2*a +3
    for k in range(2*a**2 + 6*a +3,s,2*p):
        isprime[k]=False

for i in range(0,s):
    if isprime[i]:
        primes.append(2*i +3)
        m(i,s)
print(primes)"""