# Time O(n)
def dutch_flag_partition(pivot_index: int, A: list[int]) -> list[int]:
    left_border = 0
    right_border = len(A) - 1
    index = 0
    pivot = A[pivot_index]
    while index <= right_border:
        if A[index] > pivot:
            A[index], A[right_border] = A[right_border], A[index]
            right_border -= 1
        elif A[index] < pivot:
            A[index], A[left_border] = A[left_border], A[index]
            left_border += 1
            index += 1
        else:
            index += 1
    return A


# print(dutch_flag_partition(pivot_index=3, A=[0, 1, 2, 0, 2, 1, 1]))
print(dutch_flag_partition(pivot_index=52, A=[0, 0, 1, 2, 0, 0, 1, 0, 1, 2, 0, 0, 2, 2, 1, 0, 2, 0, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 2, 0, 0, 1, 1, 1, 1, 1, 2, 1, 0, 1, 2, 1, 2]))
