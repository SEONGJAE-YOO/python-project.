n = int(input())

data = list(map(int, input().split()))

data.sort(reverse= True)
print(data)

# 7
# 11 55 22 44 33 14 22
# [55, 44, 33, 22, 22, 14, 11]
