# def checkFruitsList (fruits):
#     fruit = []
#     if not fruits:
#         return "no fruits given"
#     if("apple" in fruits and "banana" in fruits):
#          fruit.append("You got both apple and banana! ✅")

#     if "blackcurrant" in fruits or "jack fruit" in fruits:
#          fruit.insert(1,"blackcurrant", "jack jruit" )

#     fruit.extend(fruits)
#     return fruits

# fruits_Result = checkFruitsList(["apple", "banana","Dragon fruit", "JackFruit"])
# print(fruits_Result)

num = (1,2,3,4,5,7)
myList = list(num)
for i in myList:
    if(i < 6):
        print(f"'{i} is less than 6")
    if (i > 6):
        print(f"{i} is greater than 6")

print(f'This is a copy of a tuple list{myList}')
