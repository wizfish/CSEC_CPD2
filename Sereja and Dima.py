n=int(input())
cards=list(map(int,input().split()))

l=0 
r=n-1
s=0
d=0
while r>l:
    if cards[r]>=cards[l]:
        s+=cards[r]
        r-=1
    else:
        s+=cards[l]
        l+=1

    if cards[r]>=cards[l]:
        d+=cards[r]
        r-=1
    else:
        d+=cards[l]
        l+=1
if n%2==1:
    s+=cards[r]
        
        
print(s,d)
