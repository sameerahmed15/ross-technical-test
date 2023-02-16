def partial_flip(number_list, k):
    sub_array = [0 for i in range(k)]
    for i in range(k):
        sub_array[i] = number_list[i]

    flipped_array = sub_array[::-1]

    for i in range(k):
        number_list[i] = flipped_array[i]

    # for i in number_list:
    #     print(i)
    
    return number_list


def sorting(number_list):
    max_num = max(number_list)
    min_num = min(number_list)
    
    last = len(number_list)

    for i in range(len(number_list)):
        for j in range(len(number_list)):
            if number_list[j] == max_num:
                number_list =  partial_flip(number_list, j+1)
                max_num = max_num - 1
                number_list = partial_flip(number_list, last)
                last = last - 1
                for x  in number_list:
                    print(x)

    

          


sorting([3,2,4,1])

#Strategy
#[3,2,4,1] min = 1, max = 4
#[1,4,2,3] min = 2, max = 4
#[4,1,2,3] min = 2, max = 3
#max is at first index implies flip from last
# last --
#[3,2,1,4]
#max is at first index implies flip from last
#[1,2,3,4]

#Strategy #2
#Flip from the maximum number index. Bring max num to index 0
#then flip from last element so that the max is at the end of list
#Decrement max and last everytime they are used as index for flipping
#[3,2,4,1] max = 4 ; last = 4
#[4,2,3,1] max = 3 ; last = 4
#[1,3,2,4] max = 3 ; last = 3
#[3,1,2,4] max = 2 ; last = 3
#[2,1,3,4] max = 2 ; last = 2
#[1,2,3,4] max = 1