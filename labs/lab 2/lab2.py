def max_list_iter(int_list):
    if int_list == None:
        raise ValueError
    if len(int_list) == 0:
        return None
    max = int_list[0]
    for i in int_list:
        if max < i:
            max = i

    return max

def reverse_rec(int_list):
    if int_list == None:
        raise ValueError
    if int_list == []:
        return []
    else:
        return [int_list.pop()] + reverse_rec(int_list)

def bin_search(target, low, high, int_list):
    if int_list == None:
        raise ValueError
    if len(int_list) == 0:
        return None
    elif high >= low:
        mid = (high + low) // 2
        if int_list[mid] == target:
            return mid
        elif int_list[mid] > target:
            return bin_search(target, low, mid - 1, int_list)
        else:
            return bin_search(target, mid + 1, high, int_list)
    else:
        return None