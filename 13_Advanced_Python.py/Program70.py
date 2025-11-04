# Write a program to filter a list of numbers which are divisible by 5.
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
def div(n):
    if (n%5==0):
        return True
    return False
onlydiv=filter(div,a)
print(list(onlydiv))