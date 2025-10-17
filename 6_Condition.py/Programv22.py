# Write a program to detect these spams.
# "Make a money", "buy  now","subscribe now"

p1="Make a money"
p2="Buy now"
p3="Subscribe now"

a=str(input("Enter a comment"))
if((p1 in a)or (p2 in a) or (p3 in a) ):
    print("The comment is spam")
else:
    print("The comment is geniune")