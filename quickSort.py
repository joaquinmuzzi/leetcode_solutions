from typing import List


def quickSort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    pivot = arr[int(len(arr) // 2)]
    left = []
    right = []
    for i in range(len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] > pivot:
            right.append(arr[i])
    return quickSort(left) + [pivot] + quickSort(right)

print(quickSort([3, 6, 8, 10, 1, 2, 1]))
