def bubble_sort(unsorted_list, ascending = True):

    unsorted_list = unsorted_list.copy()
    count = 0

    while count < len(unsorted_list)+1 :

        for i in range(len(unsorted_list)-1):
            if unsorted_list[i] > unsorted_list[i+1]:
                temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[i+1]
                unsorted_list[i+1] = temp

        count += 1
    if ascending:
        return unsorted_list
    else:
        return unsorted_list[::-1]


def selection_sort(unsorted_list, ascending = True):

    unsorted_list = unsorted_list.copy()
    position_index = 0

    for i in range(len(unsorted_list)-1):
        min_val = unsorted_list[i+1:][0]
        min_index = 0
        for index, val in enumerate(unsorted_list[i+1:]):
            if val < min_val:
                min_val = val
                min_index = index

        min_index = i + 1 + min_index

        if unsorted_list[i] > min_val:
            unsorted_list[min_index] = unsorted_list[i]
            unsorted_list[i] = min_val

    return unsorted_list

if __name__ == "__main__":

    array = [5, 1, 4, 2, 8]
    print("Non sorted array")
    print(array)

    sorted_array = bubble_sort(array, True)
    print("Now array has been sorted in an ascending order using Bubble Sort")
    print(sorted_array)

    sorted_array = bubble_sort(array, False)
    print(sorted_array)

    array_ = [64, 25, 12, 22, 11]
    sorted_array_ = selection_sort(array_)
    print(sorted_array_)