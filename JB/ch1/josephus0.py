from collections import deque
n, k = map(int, input().split())

nums = [i for i in range(1, n+1)]
nums = deque(nums)
cnt = 0
result = []

while cnt < n :
    nums.rotate(-(k-1))
    result.append(str(nums.popleft()))
    cnt += 1

print(f'<{", ".join(result)}>')

# print("<", end="")
# for j in range(len(result)) :
#     if j < len(result) - 1:
#         print(result[j], end=", ")
#     else :
#         print(result[j], end="")
# print(">")
