# Write a program to find out whether a given post is talking about "Raman " or not.

a=str(input("Enter a post caption of facebook:"))

if( "Raman".upper() in a.upper()):
    print("The given caption is about  Raman")
else:
    print("The given caption is not about Raman")