
def Binary_Search(array, value):

    low = 0

    high = int(len(array)) - 1

    while (high - low) > 0 :
        mid = int((high + low)/2)

        if array[mid] == value:
            return True

        elif value < array[mid]:
            high = mid - 1

        elif value > array[mid]:
            low = mid + 1

    return False


if __name__ == "__main__":

    arr = [7, 1, 5, 0, 10, 10, 1, 100, 115, 56, 9, 2, 7, 4, 2, 77, 59, 246]
    print('arr:', arr)

    sorted_array = arr.sort()
    print('sorted arr:', arr)
    Binary_Search(sorted_array, 7)
    Binary_Search(sorted_array, 150)

    print('7 is in sorted arr:', Binary_Search(sorted_array, 7))
    print('150 is in sorted arr:', Binary_Search(sorted_array, 150))


