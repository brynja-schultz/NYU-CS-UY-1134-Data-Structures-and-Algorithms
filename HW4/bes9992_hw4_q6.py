def appearances(s, low, high):
    char_dict = {}
    if low == high:
        char_dict[s[low]] = 1
        return char_dict
    elif low < high:
        char_dict.update(appearances(s, low + 1, high))
        if s[low] in char_dict:
            char_dict[s[low]] += 1
            return char_dict
        else:
            char_dict[s[low]] = 1
            return char_dict

