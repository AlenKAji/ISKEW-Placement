N=int(input("Enter the value of N: "))
b=[[0 for i in range(N)] for j in range(N)]  # N*N matrix initialized with 0
def isAttacking(i,j):
    for k in range(0,N):
        if(b[i][k]==1 or b[k][j]==1):
            return True
   
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j or k-l==i-j):
                if (b[k][l] == 1):
                    return True
    return False

def nQueens(n):
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            if (b[i][j]==0 and not isAttacking(i,j)):
                b[i][j]=1
                if nQueens(n-1):
                    return True
                b[i][j]=0
    return False

print(nQueens(N))
for i in b:
    print(i)