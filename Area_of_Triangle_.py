x,y,z=map(int,input().split())
a=x+y+z
b=a/2
c=b*(b-x)*(b-y)*(b-z)
d=c**0.5
print('{:.2f}'.format(d))