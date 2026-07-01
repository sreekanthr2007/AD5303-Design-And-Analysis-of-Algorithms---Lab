def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:

        if arr[low] == arr[high]:
            if arr[low] == target:
                return low
            return -1

        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1


# Example
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 70

index = interpolation_search(arr, target)

if index != -1:
    print("Found at index:", index)
else:
    print("Not found")