# Write a program to mine a log file and find whether python is present from ques 6.

with open(f"Learning-Python/9_File_Handling.py/program46.log") as f :
    text=f.read()


if ("Python" or "python" in text):
    print("The python is present in the text")
else:
    print("The python is not present in the text.")

with open(f"Learning-Python/9_File_Handling.py/program46.log") as f :
    lines=f.readlines()

lineno = 1
for line in lines:
    if ("Python"  in line) or ("python" in line):
        print(f"The python is in line no {lineno}")
        break
    lineno += 1
else:
    print("The python is not present in the text")