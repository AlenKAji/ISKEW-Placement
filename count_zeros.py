n=int(input())
"""res=0
digit=1
while(True):
    perval,rem=divmod(n,digit)
    prefix,perval=divmod(perval,10)
    if(prefix==0):
        print(res)
    if(perval==0):
        res+=(prefix-1)*digit+rem-1
    else:
        res+=prefix*digit
"""
ab=""
for i in range(n+1):
    ab+=str(i)
print(ab.count("0"))