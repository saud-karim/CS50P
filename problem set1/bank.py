x = input("Greeting: ").strip()

if "Hello" in x or "hello" in x:
    print("$0")
elif x[0] == "h" or x[0] == "H":
    print("$20")
else:
    print("$100")
