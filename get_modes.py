def get_modes(nums):
    modes = set()
    dict_ints = {}

    for num in nums:
        dict_ints[num] = dict_ints.get(num, 0) +1
    
    max_count = max(dict_ints.values())
    for key in dict_ints:
        if dict_ints[key] == max_count:
            modes.add(key)
    print("max_count:", max_count)
    print("dict_ints:", dict_ints)

    return modes