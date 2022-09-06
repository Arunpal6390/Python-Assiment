#9. Write a python script to print cubes of first N natural numbers
x=int(input("Enter a number: "))
i=1
while i<=x:
    print(i**3,end=',')
    i=i+1