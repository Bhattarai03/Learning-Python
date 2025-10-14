# String slicing

'Raman'    # single quoted string
"Raman"    # Double quoted string
'''Raman'''# Triple quoted string

# Example
a="Raman"
nameshort=a[0:3]
print(nameshort)
# a[0:3] is same as a[-3:-5]
# a[:4] is same as a[0:4]
# a[-5:] is same as a[-5:-1]
# Negative counting is when you count from backside of the name.
# we can simply leave an empty space for "0" and "-1"
# We cannot replace "raman" by "Namar"  bu using a[-1:-5]

d=a[-5:-1]
print(d)

d="123456789"
e=d[1:6:3]
# a[1:6] represent 2,3,4,5,6 and remaining :3 represent let first number from 1:6 as it is i.e. 2 and count three until the number is finished .
# On whatever number counting 3 fall add to the first number 
# 1:6 =23456
# :3 =25 i.e on counting 3 it strikes 5 .we should do counting until the number is finished.
# answer is 25,where 2 is the first letter while 5 is the number that come form counting
print(e)

# String Function
x="raman is hero"

print(len(x)) # It is used to count the length of the string.i.e 5 here,
print(x.endswith("man") )# It is used to check whether the name ends with Man or not
print(x.startswith("Ram"))# It is used to check whether the name starts with Ram or not
print(x.capitalize()) # It is used to capitalize the  first letter of the string
print(x.title())  # It is used to capitalize the first letter of the world in the  entire sentences
print(x.replace("hero","brilliant"))


# Escape sequence
a="I am lucky the racer \n Hello lucky \t How are you lucky \n \'Mount Everest'is the tallest mountain peak in the world"
print(a)