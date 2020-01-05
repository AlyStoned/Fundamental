def binary_search(arr, guess):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        curr = arr[mid]

        if curr == guess:
            return mid
        elif curr > guess:
            high = mid - 1
        else:
            low = mid + 1

    return None


if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9]
    print(binary_search(lst, 3))
    print(binary_search(lst, 1))
    print(binary_search(lst, 18))
    print(binary_search(lst, 7))
