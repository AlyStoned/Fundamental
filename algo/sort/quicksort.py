def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [i for i in arr[1:] if i <= pivot]
    right = [i for i in arr[1:] if i > pivot]
    return quicksort(left) + [pivot] + quicksort(right)


if __name__ == '__main__':
    lst = [5, 1, 3, 5, 7, 9, 2]
    print(quicksort(lst))
