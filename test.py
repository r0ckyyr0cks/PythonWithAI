count = 0
for x in range(1, 10):
    if x % 2 == 0:
        count += 1
        print(f"{x} is even")
    else:
        print(f"{x} is odd")
print(f"We have {count} even numbers")
print("^ " * 45)
