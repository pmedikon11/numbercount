x=int(input('Pick a number: '))
b=x
e=x
z=x
if x%2 == 0:
    print('the next 5 even numbers are: ')
    for y in range(0,5):
        x=x+2
        print(x)
if e%2 == 0:
    print('the next 5 odd numbers are: ')
    for m in range(0,5):
        n=e+1
        e=e+2
        print(n)

if x%2 !=0:
    print('the next 5 even numbers are: ')
    for d in range(0,5):
        c=b+1
        b=b+2
        print(c)
if x%2 != 0:
    print('the next 5 odd numbers are: ')
    for k in range(0,5):
        z=z+2
        print(z)
