number = 100
while number > 0:
    print(number)
    number //= 2  # this is similar to "number = number / 2"
print("^" * 90)
command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
print("^" * 90)
while True:
    command = input(">")
    if command.lower() == "quit":
        break
