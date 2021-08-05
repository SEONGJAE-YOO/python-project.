#리스트는 [] 사용하고 튜플은 ()을 사용함
t2 = ('a','b',('a','b'))

print(t2)



# # 수정 불가 확인 error
# t[0]
# [out] IndexError: tuple index out of range

# t[-1]
# [out] IndexError: tuple index out of range
 
# # 튜플의 원소를 변경 안됨
# t[0] = 3
# [out] TypeError: 'tuple' object does not support item assignment

### 집합은 {}
# # 1, 2, 3을 원소로 가지는 집합을 만들어 봅시다.
# s = {1,2,3}
# type(s)
# [out] set

# # 읽을 수 없다 = 인덱싱이 안된다.
# s[1] 
# [out] TypeError: 'set' object is not subscriptable

# 튜플은 슬라이싱으로 조회가능 
# 튜플 [start,end,step]

num =(1,2,3,4,5,6)
print(num[1:3])
print(num[1:])
print(num[:-2])

print(num[::2]) #step 이 2
print(num[::-2])

# ('a', 'b', ('a', 'b'))
# (2, 3)
# (2, 3, 4, 5, 6)
# (1, 2, 3, 4)
# (1, 3, 5)
# (6, 4, 2)

