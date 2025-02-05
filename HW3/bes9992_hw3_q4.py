def remove_all(lst, value):
    left = 0
    right = 0
    num_removed = 0

    while right < len(lst):
        if lst[right] != value:
            lst[left] = lst[right]
            left += 1
            right += 1
        else:
            right += 1
            num_removed += 1

    for i in range(num_removed):
        lst.pop()


