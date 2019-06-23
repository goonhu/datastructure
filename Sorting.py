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


def MergetSort(unsorted_list, asceding = True):

    unsorted_list = unsorted_list.copy()
    mid = int((len(unsorted_list)/2))


    if len(unsorted_list) > 1:

        left = unsorted_list[:mid]
        right = unsorted_list[mid:]

        MergetSort(left)
        MergetSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                unsorted_list[k] = left[i]
                i += 1
            else:
                unsorted_list[k] = right[j]
                j += 1
            k += 1
    
    return unsorted_list

def QuickSort1(unsorted_array):
    # lomuto algorithm (pivot is the first argument)
    unsorted_array = unsorted_array.copy()
    list_length = len(unsorted_array)

    if (list_length <= 1):
        return unsorted_array
    else:
        pivot = unsorted_array[0]
        Greater = [element for element in unsorted_array[1:] if element > pivot]
        Lesser = [element for element in unsorted_array[1:] if element <= pivot]

    return QuickSort1(Lesser) + [pivot] + QuickSort1(Greater)

def QuickSort2(unsorted_array):
    # lomuto algorithm (pivot is the last element)

    unsorted_array = unsorted_array.copy()
    list_length = len(unsorted_array)

    if (list_length <= 1):
        return unsorted_array
    else:
        pivot = unsorted_array[-1]
        Greater = [element for element in unsorted_array[:-1] if element > pivot]
        Lesser = [element for element in unsorted_array[:-1] if element <= pivot]

    return QuickSort2(Lesser) + [pivot] + QuickSort2(Greater)


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

    sorted_array_1 = QuickSort1(array)
    sorted_array_2 = QuickSort2(array)
    print(sorted_array_1)
    print(sorted_array_2)