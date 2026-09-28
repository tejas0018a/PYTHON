#program 59
numbers = [10, 15, 20, 25, 30, 35]

count = 0

for n in numbers:
    if n % 2 == 0:
        count = count + 1

print("Even numbers =", count)