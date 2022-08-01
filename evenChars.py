print("Orginal String is  pynative")
print("Printing only even index chars")


original = "Valerii"
def evalse(something):
    j = 0
    for i in something:
        eval_check = j % 2
        if eval_check == 0:
            print(i,j)
        j += 1

evalse(original)