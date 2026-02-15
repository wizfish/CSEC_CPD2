k,r=map(int,input().split())
n=1

while 1:
    if (k*n)%10==0 or (k*n)%10==r:
        break
    n+=1
    
print(n)
