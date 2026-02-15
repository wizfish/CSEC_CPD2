n=int(input())
l=0
for _ in range(n):
    p,v,t=map(int,input().split())
    s=p+v+t
    if s>1:
        l+=1
print(l)
