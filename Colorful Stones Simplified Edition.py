s=input()
t=input()
curr=1
j=0
for i in range(len(t)):
    if s[j]==t[i]:
        curr+=1
        j+=1
print(curr)
