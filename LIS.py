n=int(input())
su=list(map(int,input().split(' ')))

L= [0]*n
v= [0]*n

for i in range(n):
	L[i]=1
	v[i]=-1
	for j in range(i):
		if su[j]<su[i] and L[j]+1>L[i] :
			L[i] = L[j]+1
			v[i]=j

print(max(L))
