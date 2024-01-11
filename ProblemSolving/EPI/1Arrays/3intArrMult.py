# Time O(len(num1) * len(num2))
# Space (len(num1) + len(num2))
def multiply(num1: list[int], num2: list[int]) -> list[int]:
    is_negative = num1[0] * num2[0] < 0
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])

    result = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    while result[0] == 0 and len(result) > 1:
        result.pop(0)

    result[0] *= -1 if is_negative else 1
    return result

if __name__ == '__main__':
    num1 = [0]
    num2 = [-1, 0, 0, 0]
    print(multiply(num1, num2))