#Counting vowels in a string using classes and objects

x = input("Would you love to play with minors😍 : ")
answer = x == "yes" and x == "no"

for char in x :
    if x == "yes":
        print("Nice choice, Btw we are jus countin vovels dude, nothin else, so dont get any ideas😏")
        if x == "no":
            print("Aww, Bhosdi ke, why not?😔")

count = 0

for i in x:
    if i in "aeiouAEIOU":
        count += 1


print("Btw....the count of vowels is:", count)