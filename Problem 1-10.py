x = 0
for i in range(1000):
    if(i%3==0 and i%5==0):
        x+=i
    elif(i%3==0):
        x+=i
    elif(i%5==0):
        x+=i

a,b,c,x=1,1,0,0
while(x<4000000):
    c=a+b
    print(c)
    b=a
    a=c
    if(c%2==0):
        x+=c
print(x)