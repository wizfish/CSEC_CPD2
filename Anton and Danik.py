n=int(input())
s=input()
D=s.count('D')
A=s.count('A')
if A>D:
    print("Anton")
elif D>A:
    print("Danik")
else:
    print("Friendship")
