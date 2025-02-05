def find_duplicates(lst):
    dict = {}
    duplicate = []

    for i in range(len(lst)):
        if not lst[i] in dict:
            dict[lst[i]] = 1

        else:
            if dict[lst[i]] == 1:
                duplicate.append(lst[i])
            dict[lst[i]] += 1

    return duplicate
