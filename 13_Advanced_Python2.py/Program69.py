# A list contains the multiplication table of 7 .Write a program to convert  it in to vertical strings of same number.
table=[str(7*i) for i in range(1,11)]
b="\n".join(table)
print(b)