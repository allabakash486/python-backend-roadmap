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
