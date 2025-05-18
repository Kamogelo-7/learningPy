import os
try:
    # Try to open msg.txt
    res = "msg.txt"
    with open(res, "r") as f:
        msg_content = f.read()
        print("msg.txt content:")
        print(msg_content)

    if os.path.exists(res):
        print(f"file {res} is exist")
    else:
        print(f"File path of {res} does not exist")

    # Try to open pythonConcepts.txt
    with open("pythonConcepts.txt", "r") as file2:
    # By default read() method only returns all the text content, but can also specify the amout or char to output
        concepts_content = file2.readline()
        print("pythonConcepts.txt content:")
        print(concepts_content)

    #Writing into existing files
    with open("pythonConcepts.txt", "a") as f:
         f.write("Yoooooh, thusang bathong ba bolaya di mpya ka mo nextdoor\n aowa bathong yoh, yoh,yoh le di katse on a serious level ke bona mathata ka mo yasis!")


    with open("pythonConcepts.txt") as f:
        print(f.read())


except FileNotFoundError as e:
    print(f"File not found: {e.filename}")

except Exception as e:
    print(f"An error occurred: {e}")

