# function in python
def simpleInterest(p, r, t):
    si = (p * r * t) / 100
    print("Simple Interest is:", si)
    # return si


principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time in years: "))
simpleInterest(principal, rate, time)
# simpleInterest(1000, 5, 3)
# simpleInterest(1500, 4, 5)


def cube(n):
    cube_value = n * n * n
    return cube_value


num = int(input("Enter a number to find its cube: "))
result = cube(num)
print("Cube of", num, "is:", result)
