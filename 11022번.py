n=input()
n=int(n)
data=[]
for i in range(0,n):
    first,second=map(int,input().split())
    data.append(first)
    data.append(second)

for i in range(0,n):
    print("Case #{}: {} + {} = {}".format(i+1,data[2*i],data[2*i+1],data[2*i]+data[2*i+1]))
