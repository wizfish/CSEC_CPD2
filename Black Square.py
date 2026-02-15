a=list(map(int,input().split()))
s=list(map(int,input()))
ans=0

for i in s:
    ans+=a[i-1]

print(ans)

