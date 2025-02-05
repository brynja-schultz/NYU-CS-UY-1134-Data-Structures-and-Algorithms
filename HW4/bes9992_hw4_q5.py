def count_lowercase(s, low, high):
    if low == high:
        if s[low].islower():
            return 1
        return 0

    else:
        if s[low].islower():
            return 1 + count_lowercase(s, low + 1, high)

        return count_lowercase(s, low + 1, high)


def is_number_of_lowercase_even(s, low, high):
    if low == high:  # Base Case  ONE CHARACTER
        if s[low].islower():
            return False
        return True

    elif low < high:
        sub_problem = is_number_of_lowercase_even(s, low + 1, high)

        if sub_problem:  # sub is even
            if s[low].islower():  # first character is lower, total is odd
                return False
            return True  # first character is upper, total is even

        else:  # sub is odd
            if s[low].islower():  # first is lower, total is even
                return True
            return False  # first is upper, total is odd


