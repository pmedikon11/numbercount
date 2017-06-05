# numbercount
x=5
print('The next 5 even numbers are: ')
#The if block is for detecting if the number is odd or even
if x%2 != 0:
    x=x+1
    #This statement prints the first even number after input 
    print(x)
#This loop will add 2 to the new x value 5 times
for y in range(0,5):
    x=x+2
    print(x)
print('The next 5 odd numbers are: ')
#This loop wil add 1 to the odd value and then add 2, 5 times
c=x
for d in range(0,5):
    b=c+1
    c=c+2
    print(b)
