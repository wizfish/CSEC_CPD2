n=int(input())
a=[0]*n
ans=1
for i in range(n):
    s=input()
    a[i]=s
for i in range(1,n):
    if a[i]!=a[i-1]:
        ans+=1
        continue

print(ans)

    
