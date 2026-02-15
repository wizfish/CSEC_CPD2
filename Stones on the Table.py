00
n=int(input())
s=input()
mn=0
for i in range(1,n):
    if s[i]==s[i-1]:
        mn+=1
print(mn)
