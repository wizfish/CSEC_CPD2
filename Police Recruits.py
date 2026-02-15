n=int(input())
a=list(map(int,input().split()))
p=0
l=0

for i in range(n):
    if a[i]!=-1:
        p+=a[i]
    elif p>0:
            p-=1
    else:
        l+=1
    
print(l)
    
