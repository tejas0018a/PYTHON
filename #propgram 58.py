#propgram 58
numbers = [10, 25, 7, 45, 18]

smallest = numbers[0]

for n in numbers:
    if n < smallest:
        smallest = n

print("Smallest =", smallest)
