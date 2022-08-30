#10.Write a Python script to create a list, where each element of the list is a digit of a given number.
# For list of integers
lst1 = []
lst1 = [int(item) for item in input("Enter the list items : ").split()]
print(lst1)