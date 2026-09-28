#program 57
numbers = [10, 25, 7, 45, 18]

largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print("Largest =", largest)
