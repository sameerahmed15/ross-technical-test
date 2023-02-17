def partial_flip(number_list, k):
    # TODO: try to optimize this function

    sub_array = [0 for i in range(k)]
    for i in range(k):
        sub_array[i] = number_list[i]

    flipped_array = sub_array[::-1]

    for i in range(k):
        number_list[i] = flipped_array[i]
    
    return number_list


def sorting(number_list):
    # TODO: try to optimize this function

    max_num = max(number_list)
    last = len(number_list)
    k_list = []
    for i in range(len(number_list)):
        for j in range(len(number_list)):
            if max_num == 1:
                break
            elif number_list[j] == max_num:
                number_list =  partial_flip(number_list, j+1)
                k_list.append(j+1)
                max_num = max_num - 1
                number_list = partial_flip(number_list, last)
                k_list.append(last)
                last = last - 1
 
    for i in k_list:
        print(i)

    return k_list
    

sorting([3,2,4,1])