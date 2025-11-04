# Merging Dictionary
dict1={"a":1,"b":3}
dict2={"d":1,"b":5}
merged=dict1|dict2
print(merged,type(merged))

# Use multiple context managers in a single with statement more cleanly using the parenthesised context manager.
with (
    open("file1.txt") as f1,
    open("File2.txt") as f2
):
    f1.read
    f2.read
    # process the file