def partial_flip(arr, k):

    arr[0:k] = arr[k-1::-1]
    
    return arr


def sorting(arr):
    # TODO: try to optimize this function

    len_arr = len(arr)
    max_num = max(arr)
    last = len_arr
    ks = []
    for i in range(len_arr):
        for j in range(len_arr):
            if max_num == 1:
                break
            elif arr[j] == max_num:
                arr =  partial_flip(arr, j+1)
                ks.append(j+1)
                max_num -= 1
                arr = partial_flip(arr, last)
                ks.append(last)
                last -= 1

    return ks