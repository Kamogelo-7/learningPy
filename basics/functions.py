def checkFruitsList (fruits):
    fruit = []
    if not fruits:
        return "no fruits given"
    if("apple" in fruits and "banana" in fruits):
         fruit.append("You got both apple and banana! ✅")

    if "blackcurrant" in fruits or "jack fruit" in fruits:
         fruit.insert(1,"blackcurrant", "jack jruit" )

    fruit.extend(fruits)
    return fruits

fruits_Result = checkFruitsList(["apple", "banana","Dragon fruit", "JackFruit"])
print(fruits_Result)
