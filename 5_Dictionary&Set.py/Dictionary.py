d={}   # Empty dictionary
marks ={
    "raman": 100,
    "sahil":56,
    "dipesh": 45

    
}
print(marks,type(marks))
print(marks["sahil"])
  
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"raman" : 99,"Rhino":67})
print(marks.items())

# print(marks["raman2"])  # Return an error 
# print(marks.get["raman2"])  # print none

print(marks.pop("sahil"))
# It return value and remove the key value pair of specific keys
print(marks)
print(marks.popitem()) # It print the value of last inserted key pair