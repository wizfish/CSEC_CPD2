n=5
a=[]
for _ in range(n):
    a.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            print(abs(2-i)+abs(2-j))

    
