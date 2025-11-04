try:
    a=int(input("hey,Enter a number:"))
    print(a)

except Exception as e:
    print(e)
else:
    print("I am inside else")

print("Thank you")

# The condition else sucessfully run when the try is sucessfully executed.
# It means that when i enter the string in the int a , the code simply exit the else condition.
