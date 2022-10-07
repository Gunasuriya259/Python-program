print("Enter the String: ", end="")
str = input()

str = sorted(str, reverse=True)
str = ''.join(str)

print("\nSorted String in descending, is:", str)
