def shift(lst, k, direction="left"):
    if direction == "left":
        for i in range(k):
            temp = lst.pop(0)
            lst.append(temp)
    else:
        for i in range(k):
            temp = lst.pop(len(lst)-1)
            lst.insert(0, temp)

    return lst

