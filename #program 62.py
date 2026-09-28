#program 62
numbers = [10, 20, 30, 40, 50]

n = int(input("Enter number to remove: "))

if n in numbers:
    numbers.remove(n)
    print(numbers)
else:
    print("Element not found")
