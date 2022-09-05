#7. Write a python script to print first N even natural numbers in reverse order
x=int(input("Enter a number: "))
i=x
while i>=2:
    print(i,end=',')
    i=i-2

