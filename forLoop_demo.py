# break statement in for loop
for x in range(11, 50, 5):
    print(x, end=' ')
    if x == 31:
        break

print("\n" + "^ " * 45)

# continue statement in for loop
for x in range(11, 50, 5):
    if x == 31:
        continue
    print(x, end=' ')

print("\n" + "^ " * 45)
