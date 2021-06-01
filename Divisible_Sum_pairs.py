n,k =input().split(" ")
n,k=[int(n),int(k)]
arr =list(map (int,input().split()))
count=0
for i in range(n):
    for j in range(i+1,n):
        
        if i<j and (arr[i]+arr[j])%int(k)==0:
            count=count+1
print(count)
            
