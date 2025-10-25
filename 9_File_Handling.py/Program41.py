# Write a program to read the text from a given file "poem.txt" and find out whether it contain the word "Twinkle".


with open("Poem.txt") as f :
    d=f.read()
    if ("Twinkle" in d):
        print("The folder contain  word twinkle ")
    else:
        print("the file doesnot contain word twinkle")

    