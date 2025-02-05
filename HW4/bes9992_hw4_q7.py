def split_by_sign(lst, low, high):
    if low == high:
        return lst

    elif low < high:
        if lst[low] > 0 > lst[high]:  # swap negative on right with positive on left
            lst[low], lst[high] = lst[high], lst[low]
            split_by_sign(lst, low + 1, high - 1)

        elif lst[low] > 0:  # both sides are positive
            split_by_sign(lst, low, high-1)

        split_by_sign(lst, low+1, high)




