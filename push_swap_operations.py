def swap_first_two_elements(lst):
    if len(lst) > 1:
        lst[0], lst[1] = lst[1], lst[0]

    return lst