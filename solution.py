def partial_flip(number_list, k):
    test = [0 for i in range(k)]
    for i in range(k):
        test[i] = number_list[i]

    test = test[::-1]

    for i in range(k):
        number_list[i] = test[i]

    for i in number_list:
        print(i)

partial_flip([3,2,1,4], 3)