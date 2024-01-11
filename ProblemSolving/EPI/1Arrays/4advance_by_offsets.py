# Time O(n)
# def can_reach_end(A: list[int]) -> bool:
#     cost = 0
#     for i in reversed(range(len(A))):
#         if A[i] >= cost:
#             cost = 0
#         cost += 1
#     return cost == 1

# Alternate
# Time O(n)
def can_reach_end(A: list[int]) -> bool:
    max_reach, last_index = 0, len(A) - 1
    index = 0
    while index <= max_reach < last_index:
        max_reach = max(max_reach, index + A[index])
        index += 1
    return max_reach >= last_index


A = [3, 3, 1, 0, 2, 0, 1]
# A = [3, 2, 0, 0, 2, 0, 1]
print(can_reach_end(A=A))
