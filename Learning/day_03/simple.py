def simple():
    print("This is a simple function.")
simple()

def find_largest_number_in_array(arr):
    if not arr:
        return None
    largest = arr[0]
    for ele in range(1, len(arr)):
        if arr[ele] > largest:
            largest = arr[ele]
    return largest
array = [1, 2, 3,4,4]
print(find_largest_number_in_array(array))

def find_smallest_number_in_array(arr):
    if not arr:
        return
    smallest = arr[0]
    for ele in range(1, len(arr)-1):
        if arr[ele] < smallest :
            smallest = arr [ele]
    return smallest
array = [1, 2, 3, 4, 5]
print(find_smallest_number_in_array(array))

def find_second_largest_number_in_array(arr):
    if len(arr) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num
    return second_largest
array = [1,2,3,4,5]
print(find_second_largest_number_in_array(array))

def sort_array(arr):
    if len(arr) < 2:
        return arr

    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(sort_array(array))