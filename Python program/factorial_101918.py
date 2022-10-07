def find_factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


x = int(input("Enter a number: "))

result = find_factorial(x)

print("Factorial is:", result)
