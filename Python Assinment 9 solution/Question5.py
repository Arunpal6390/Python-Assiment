#5. Write a python script to print first N odd natural numbers in reverse order
x=int(input("Enter a number: "))
i=x
while i>=1:
    print(i,end=',')
    i=i-2
