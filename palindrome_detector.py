def reverse_something(something):
    print("The given variable is :", something)
    str_some = str(something)
    str_len = len(str_some)
    rev_str = str_some[-1:-(str_len + 1):-1]
    for i in rev_str:
        print(i, end=" ")

palindrome_detector("fgdfgd")






