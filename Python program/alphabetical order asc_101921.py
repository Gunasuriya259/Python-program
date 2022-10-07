print("Enter the String: ", end="")
str = input()

str = sorted(str, reverse=False)
str = ''.join(str)

print("\nSorted String in ascending, is:", str)
