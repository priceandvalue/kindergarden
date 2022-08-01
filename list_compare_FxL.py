def divised_by(list_place, divise_number):

    print("Given list is :", list_place)
    print("Divised by ", divise_number)

    for i in list_place:
        last = i % divise_number
        if last == 0:
            print(i)
user_range_list = list(range(156))
user_div_number = int(input("Enter div number "))
divised_by(user_range_list, user_div_number)

