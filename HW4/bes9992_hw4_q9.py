def permutations(lst, low, high):
    perm_list = []

    if low == high:
        return [[lst[low]]]

    elif low < high:
        sub_problem = permutations(lst, low, high - 1)

        for j in range(low, high+1):

            for item in sub_problem:
                copy_sub_problem = [y for y in item]
                copy_sub_problem.insert(j, lst[high])
                perm_list.append(copy_sub_problem)

    return perm_list

