# Expection is used  for not crashing the code despite having error in it .
try:
    a=int(input("hey,Enter a number:"))
    print(a)

except Exception as e:
    print(e)


print("Thank you")

# In this code if i enter the string in int a it doesnot crash the program despite having an error .it also print Thank you the end