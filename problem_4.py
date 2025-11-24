def dictionary(key_list, value_list):
    my_dict = {}
    if type(key_list) != list or type(value_list) != list:
        print("ERROR")
        return None
    if len(key_list) != len(value_list):
        print("ERROR: lengths do not match")
        return None

    for i in range(len(key_list)):
        my_dict[key_list[i]] = value_list[i]

    return my_dict

arr = ['apple', 'grape', 100, 3.4, (1, 2), (2, 3)]
arr1 = ['apple', 'grape', 100, 3.4, [1, 2], (2, 3)]
#NB: key can not be a list, dictionary or set
D = dictionary(arr, arr1)
print(D)
