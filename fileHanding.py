try:
    # Try to open msg.txt
    res = "msg.txt"
    with open(res, "r") as f:
        msg_content = f.read()
        print("msg.txt content:")
        print(msg_content)

    # Try to open pythonConcepts.txt
    with open("pythonConcepts.txt", "r") as file2:
        concepts_content = file2.read()
        print("pythonConcepts.txt content:")
        print(concepts_content)

except FileNotFoundError as e:
    print(f"File not found: {e.filename}")

except Exception as e:
    print(f"An error occurred: {e}")

