v1,v2=map(int,input().split())
char3=input().split()
d4=[]
for h in char3:
	if(int(h)%2!=0):
		d4.append(h)
print(d4[v2-1])
