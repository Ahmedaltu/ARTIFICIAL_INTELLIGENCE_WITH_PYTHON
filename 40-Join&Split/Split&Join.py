
def my_split(string, sep):
    list1 = []
    word = ''

    for c in string:
        if c not in sep:
            word += c
        elif word:
            list1.append(word)
            word = ''
    if word:
        list1.append(word)

    return list1


def my_join(lst, sep):
    str = ''

    for item in lst:
        if item == lst[len(lst)-1]:
            str = str + item
        else:
            str = str + item + sep

    return str


sentence = str(input("Please enter sentence: "))
print(my_join(my_split(sentence, ' '), ','))
print(my_join(my_split(sentence, ' '), '\n'))



