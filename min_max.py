n=map(int,input().split())
x=list(n)
x.sort()
print(sum(x[0:len(x)-1]),sum(x[1:]))
