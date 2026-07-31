key_days = {
    "Mon" : "Monday",
    "Tue" : "Tuesday",
    "Wed" : "Wednesday",
    "Thu" : "Thursday",
    "7" : "Friday",      #You can also access keys through numbers...
    "Sat" : "Saturday",
    "Sun" : "Sunday",
}

print(key_days["Mon"])
print(key_days["Wed"])
print(key_days["Sun"])

#One more method to print ts

print(key_days.get("7"))

#Set Not Valid

print(key_days.get("Lov" , "Not a valid key in dataset...."))



