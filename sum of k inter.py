u=list(map(int,input().split()))
t=list(map(int,input().split()))
k=u[1]
s=0
for i in range(0,k):
    s+=t[i]
print(s)
