#program 71
text = input("Enter a string: ")

count = 0

for ch in text:
    if ch == " ":
        count = count + 1

print("Number of spaces =", count)
