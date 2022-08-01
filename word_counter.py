def word_counter(a_string, a_word):
    string_list = list(a_string.split(" "))
    i = 0
    for sep_word in string_list:
        if sep_word == a_word:
            i += 1
    print(f"{a_word} appears {i} times in that string")

str_x = "Emma is good developer. Emma is a writer."
word_for_search = "Emma"
word_counter(str_x, word_for_search)





