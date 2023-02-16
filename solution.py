def partial_flip(number_list, k):
    sub_array = [0 for i in range(k)]
    for i in range(k):
        sub_array[i] = number_list[i]

    flipped_array = sub_array[::-1]

    for i in range(k):
        number_list[i] = flipped_array[i]

    for i in number_list:
        print(i)

partial_flip([3,2,1,4], 3)