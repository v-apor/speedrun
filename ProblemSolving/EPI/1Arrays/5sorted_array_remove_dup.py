# Simplest was, push everything in set and return the length
# Time O(n) | Space O(n)
# def delete_duplicates(A: list[int]) -> int:
#     return len(set(A))


# Time O(n) | Space O(1)
def delete_duplicates(A: list[int]) -> int:
    write_index = 1
    position = 1
    while position < len(A):
        if A[write_index - 1] != A[position]:
            A[write_index] = A[position]
            write_index += 1
        position += 1
    return  write_index


A = [2, 3, 5, 5, 7, 11, 11, 11, 13, 13, 17, 19, 23]
print(delete_duplicates(A))