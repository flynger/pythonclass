def convert_list(lst):
    newList = []
    for item in lst:
        if type(item) == list:
            for i in convert_list(item):
                newList.append(i)
        else:
            newList.append(item)
    return newList

data = [[11, 13],15,18,[12, 13, [12, 13, [12, [12, 13,[],[], [12, 13, 15]], 15]]]]
print(convert_list(data))