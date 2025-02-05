def list_min(lst, low, high):
    if low == high:
        return lst[low]

    elif low < high:
        if lst[low] <= lst[high]:
            return list_min(lst, low, high - 1)

        else:
            return list_min(lst, low + 1, high)

