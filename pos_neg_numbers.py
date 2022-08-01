def posneg(val):
    if int(val.strip()):
        digit_list = list(val.strip())
        for digit_list[0] in digit_list:
            if digit_list[0].isdigit():
                print("It's a positive number")
                break
            else:
                print("It's a negative number")
                break
    else:
        print("Try again and follow the insructions")


user_input = input("Enter positive or negative number : ")
posneg(user_input)