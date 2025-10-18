# Write a recursive function to calculate the sum of first n natural numbers.
a=int(input("Enter a number:"))

def rec(a):
    if a==1:
        return 1
    return a + rec(a-1)
print(f"The sum of first {a} number is ",rec(a))