# Time O(n) | Space O(1)
def plus_one(A: list[int]) -> list[int]:
    index = len(A) - 1
    while index >= 0:
        if A[index] == 9:
            A[index] = 0
            index -= 1
            continue
        A[index] += 1
        break
    if A[index] == 0:
        A[0] = 1
        A.append(0)
    return A


print(plus_one(A=[1, 2, 9]))
print(plus_one(A=[9, 9, 9]))
