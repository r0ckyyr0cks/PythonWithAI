for number in range(1, 10, 2):
    print("Attempt", number, number * ".")
print("^" * 90)
successful = False
for num in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")
print("^" * 90)
