s=input() 
a=0
current='a'
for ch in s:
    diff=abs(ord(ch)-ord(current))
    a+=min(diff,26-diff)
    current=ch
print(a)
