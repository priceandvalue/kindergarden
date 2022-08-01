def list_compare(list_place):
        if list_place[0] == list_place[-1]:
            print("Given list :", list_place)
            print(True)
        else:
            print("Given list :", list_place)
            print(False)

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
list_compare(numbers_x)
list_compare(numbers_y)