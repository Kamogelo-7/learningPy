#Get the character at position 1 (remember that the first character has the position 0):
user = "Satohimajim"
print(user[0])

a = "Hello, World!"
print(len(a))

#Since strings are arrays, we can loop through the characters in a string, with a for loop
for x in "Satohimajim":
    print(x)

#To check if a certain phrase or character is present in a string, we can use the keyword in.
message = "heyy, how are you just checking on you 💖"
# print("💖" in message or "heyy" in message)

if "hey" and "💖" in message:
    print(f"available {message}")
else:
    print("Unavailable match not found🗿")

txt = "Nah dawg this car expensive is to for me ngl"

if "expensive" not in txt:
    print(f" Word expensive should be at index {[5]} missing word in this sentence")
else:
    print(txt)

#Pyton slicing strings: Allows to get the characters from position 2 to position 5 (not included):
txt = "Hello, World!"
Sliced_Txt = txt[2:5]
print(Sliced_Txt)
