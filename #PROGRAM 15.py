# PROGRAM 15
A = int(input("Enter The First Number: "))
B = int(input("Enter The Second Number: "))
C = int(input("Enter The Third Number: "))

if A >= B and A >= C:
    print("Greatest =", A)
elif B >= A and B >= C:
    print("Greatest =", B)
else:
    print("Greatest =", C)
