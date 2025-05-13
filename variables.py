userName = str(input("Hello! what is your name young sage?"))
userAge = int(input("Hello what is your age?"))
userJob = str(input("What type of job you work?"))
userSalary = int(input("whats your salary R10,000? or above 10k? Income:"))

if  userAge < 18 :
    print(f"HEY! {userName} you are waay under age you lol BACK OFF THIS SITE young blood🗿")

elif userAge == 21 or 22:

    print(f"Bro YOU ARE A LEGEND WISE SAGE😭💎")

else:
    print(f"hello {userName}! nice to have you here😀 i see you are {userAge} years old wise sage🐦‍🔥")

#pure function this one mate

def checkUserSalary(income, jobTitle):
    if income < 10000 and jobTitle != "Software engineer":
        return "Damn! tough times, good luck in life tho.🗿😖"
    elif income >= 10000 and jobTitle == "Software engineer":
        return "Now we talking me, lad keep winning son you hear me!!!😭💎"
    else:
        return "Different job and salary combination!"

results = checkUserSalary(userSalary, userJob.lower())
print(results)

message = "heyy, how are you just checking on you 💖"

if "hey" and "💖" in message:
    print(f"available {message}")
else:
    print("Unavailable match not found🗿")

txt = "Nah dawg this car expensive is to for me ngl"

if "expensive" not in txt:
    print(f" Word expensive should be at index {[5]} missing word in this sentence")
else:
    print(txt)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

num = (1,2,3,4,5)
myList = list(num)
print(myList)

