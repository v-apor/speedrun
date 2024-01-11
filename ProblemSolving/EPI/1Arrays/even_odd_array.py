# Time Complexity O(n) & space O(1):
def even_odd(arr: list) -> list:
    odd_ptr = len(arr) - 1
    even_ptr = 0
    while even_ptr < odd_ptr:
        if arr[even_ptr] % 2 == 1:
            arr[even_ptr], arr[odd_ptr] = arr[odd_ptr], arr[even_ptr]
            odd_ptr -= 1
        else:
            even_ptr += 1
    return arr


inp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(even_odd(inp))