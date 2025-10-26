# Write a program to detect double space in the string and replace with single space.

a=str(input("Enter a sentences:"))
b=a.find("  ")

if b>=1:
    print("Double space is detected in the sentences.")
print(a.replace("  "," "))
  # This line of code is for replacing double space into a single space.