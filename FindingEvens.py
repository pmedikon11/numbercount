#Will find and Print all even numbers between 1000 and 3000
x=1000
c={}
while x<3002:
    if x%2==0:
        c={x}
        print(c)
    x=x+1
