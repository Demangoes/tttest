a = 5
start = 1
for i in range(a):
    start +=i
    dis = i+2
    for j in range(a-i):
        if j ==0:
            print(start,end=" ")
        elif 1<=j<a-i-1:
            print(start+dis,end=" ")
            dis +=1
        else:
            print(start+dis)