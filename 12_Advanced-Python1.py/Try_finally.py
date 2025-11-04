
def main():
    try:
         a=int(input("hey,Enter a number:"))
         print(a)
         return

    except Exception as e:
        print(e)
        return
    finally:
            print("I am inside of finally")

print("Thank you")
main()
# Here the finally run every time no matter of try sucessfully executed or not
# Main use of finally is in function,where after code "return" function ended and doesnot execute code afterward but with the code"finally" it execute the code after return also.
# Simply it is used to break the rule in python.