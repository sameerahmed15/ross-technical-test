def partial_flip(arr, k):
    """Reverse a sub-array from given index

        Parameters
        ----------
        arr: list
            Array of integers from 1 to len(arr)-1
        k : int
            Index value from where the array will be reversed
    """

    arr[0:k] = arr[k-1::-1]
    
    return arr


def sorting(arr):
    """Sort a list of integers from smallest to highest

        Parameters
        ----------
        arr: list
            Array of integers from 1 to len(arr)-1
    """

    len_arr = len(arr)
    max_num = len_arr
    last = len_arr
    ks = []
    for i in range(len_arr):
        for j in range(len_arr):
            if max_num == 1:
                break
            elif arr[j] == max_num:
                # Shift max to index 0
                arr =  partial_flip(arr, j+1)
                ks.append(j+1)
                max_num -= 1
                # Shift max to last index
                arr = partial_flip(arr, last)
                ks.append(last)
                last -= 1
                break
    print("Sorted array: ", *arr)
    print("List of k values: ", *ks)

    return ks