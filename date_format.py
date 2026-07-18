#method 1
d=int(input())
m=int(input())
y=int(input())

print("%02d/"%d,end="")
print("%02d/"%m,end="")
print("%04d/"%y)



#method2
d=int(input())
m=int(input())
y=int(input())

print(d,m,y,sep="/")
