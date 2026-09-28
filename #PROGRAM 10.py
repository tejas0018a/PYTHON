#PROGRAM 10
seconds=int(input("Enter Total Seconds:"))
hours=seconds//3600
remaining=seconds%3600
minutes=remaining//60
seconds=remaining%60

print("hours=",hours)
print("minutes=",minutes)
print("seconds=",seconds)