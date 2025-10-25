# write a program to generate multiplication tables from 2 to 20 and write it to the different files.place these files in a folder for 13 years old.

def generatetable(n):
    table=""
    for i in range(1,11):
        table += f"{n}*{i}={n*i}\n"

    with open(f"Table/table_{n}.txt","w") as f:
        f.write(table)

for i in range(1,21):
    generatetable(i)
