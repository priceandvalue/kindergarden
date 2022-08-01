list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
odd_list = []
even_list = []

def odd_list_check(int_list):

    for i in int_list:
        if (i % 2) != 0:
            odd_list.append(i)

    return odd_list

def even_list_check(int_list):

    for i in int_list:
        if (i % 2) != 1:
            even_list.append(i)

    return even_list

print(odd_list_check(list1) + even_list_check(list2))

