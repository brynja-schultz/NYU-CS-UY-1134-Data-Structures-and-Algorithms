def split_parity(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        if lst[left] % 2 == 1:
            left += 1

        if lst[right] % 2 == 0:
            right -= 1

        elif lst[left] % 2 == 0 and lst[right] % 2 == 1:
            temp = lst[right]
            lst[right] = lst[left]
            lst[left] = temp

    return lst



