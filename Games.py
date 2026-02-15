n=int(input())
a=[]
ans=0
for _ in range(n):
    h=list(map(int,input().split()))
    a.append(h)

for i in range(n):
    for j in range(n):
        if a[i][0]==a[j][1]:
            ans+=1

print(ans)
