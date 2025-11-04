l=[3,33,54,234]
# index=0
# for item in l:
    
#     print(f"The item number  at index{index} is {item}")
#     index+=1

# Above code can be written as this

for index,item in enumerate(l):
    print(f"The item number  at index {index} is {item}")