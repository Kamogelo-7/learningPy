try:
    x = 1
    if x < 0:
        raise Exception("An error ocuured")
except Exception as e:
        print(f"Fix {e} value")
else:
    print(f"Value = {x}")
finally:
    print(f"Welp here you go lad {x}")

