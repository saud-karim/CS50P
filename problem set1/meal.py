
def main():
    time = input("What time is it? ").split(":")
    return time


def convert(time):
    # print(float(int(time[0]) + int(time[1])/60*1))
    t = float(int(time[0]) + int(time[1])/60*1)
    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")
    else:
        print("unknown time")

# breakfast between 7:00 and 8:00
# lunch between 12:00 and 13:00
# dinner between 18:00 and 19:00. 

convert(main())

# print(int(30)/60*1)

# if __name__ == "__main__":
#     main()