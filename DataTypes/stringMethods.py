# find - method returns the index of the first occurrence
# of the specified value
txt = "Hello, welcome to my world."
if txt.find("o") >= 0:
    print("Yes, 'o' is present at index:", txt.find("o"))

if txt.find("o", 5) >= 0:
    print("Yes, another 'o' is present at index:", txt.find("o", 5))

if txt.find("to") >= 0:
    print("Yes, 'to' is present at index:", txt.find("to"))

if txt.find("my", 10, 20) >= 0:
    print("Yes, 'my' is present at index:", txt.find("my", 10, 20))

if txt.rfind("o") >= 0:
    print("Yes, last 'o' is present at index:", txt.rfind("o"))

if txt.rfind("o", 0, 10) >= 0:
    print("Yes, another last 'o' is present at index:", txt.rfind("o", 0, 10))

# count - method returns the number of occurrences of a substring in the given string
print(txt.count("o"))
print(txt.count("o", 5, 10))

# startswith - method returns True if the string starts with the specified value
print(txt.startswith("Hello"))
print(txt.startswith("welcome", 7, 20))

# endswith - method returns True if the string ends with the specified value
print(txt.endswith("world."))
print(txt.endswith("my", 5, 20))

print(txt.upper())  # upper - method converts a string into upper case
print(txt.lower())  # lower - method converts a string into lower case
print(txt.capitalize())  # capitalize - method converts the first character to upper case