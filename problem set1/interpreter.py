num = input("Expression: ").strip().split()
x = float(num[0])
z = float(num[-1])

if "+" in num[1]:
    print(round(x + z, 1))
elif "-" in num[1]:
    print(round(x - z, 1))
elif "*" in num[1]:
    print(round(x * z, 1))
elif "/" in num[1]:
    print(round(x / z, 1))


