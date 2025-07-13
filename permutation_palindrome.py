s=input("String :")
d={}
count=0
for i in range(len(s)):
    d[s[i]]=d.get(s[i],0)+1
count=0
for k in d:
    if d[k]%2!=0:
        count+=1
print(d)
if(count>1):
    print("no")
else:
    print("yes")