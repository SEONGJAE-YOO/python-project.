#정열 알고리즘 문제 : 두배열의 원소 교체

# 두개의 배열 A, B 가 있고 각 배열은 N개의 원소로 구성되며 원소는 모두 자연수로 이루어진다. 이때 바꾸기 연산을 최대 K 번 수행할 수 있고 바꾸기 연산이란 A에 있는 원소 하나를 B에 있는 원소 하나와 바꾸는 것을 말한다. 우리의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 만들면된다.

# N, K 그리고 배열 A, B의 정보가 주어지고, 최대 K 번 바꾸기 연산이 가능할 때 가장 최대의 합을 가지는 A릐 모든 원소의 합의 최대값을 출력하는 프로그램을 작성하시오.

# 1. 입력 조건Permalink
# 첫 번째 줄: N, K 가 공백으로 구분되어 입력 (1 <= N <= 100,000, 0 <= K <= N)
# 두 번째 줄: 배열 A의 원소들이 공백으로 구분되어 입력 (원소 a < 10,000,000인 자연수)
# 세 번째 줄: 배열 B의 원소들이 공백으로 구분되어 입력 (원소 b < 10,000,000인 자연수)
# 2. 출력 조건Permalink
# 최대 K번 바꿔치기 연산을 수행해서 가장 최대의 합을 갖는 A의 모든 원소 값의 합을 출력
# 입력 예시

# 5 3
# 1 2 5 4 3
# 5 5 6 6 5
# 출력 예시

# 26

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(a)
print(b)

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i],b[i] = b[i],a[i]
    else:
        break

print(sum(a))

# #정렬 낮은 수 -> 큰수 
array = [2,6,1,3,6,9]

array.sort()
print(array)

result = sorted(array)
print(result)


# #key array 정렬

array = [('바나나',2),('사과',5),('당근',3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)


# # 문제 설명Permalink
# # N명의 학생의 성적 정보가 주어진다. 형식은 이름 성적 으로 주어지는데 이때 이들의 성적이 낮은 순으로 학생 이름을 출력하는 문제다.

# # 입력 조건Permalink
# # 첫 번째 줄에 학생의 수 N이 입력된다. (1 <= N <= 100,000)
# # 두 번째 줄 부터 N+1 번째 줄 까지 학생의 이름 그리고 성적이 공백으로 주어진다. 학생이름 길이는 100이하, 성적은 100이하 자연수로 주어진다.
# # 출력 조건Permalink
# # 모든 학생의 이름을 성적이 낮은 순으로 출력하면된다. 동일한 성적은 자유롭게 출력하면된다.
# # 입력 예시Permalink
# # 2
# # 홍길동 96
# # 이순신 78
# # 출력 예시Permalink
# # 이순신 홍길동     

n = int(input())

arr = []
for i in range(n):
    tup = input().split()
    arr.append((tup[0],int(tup[1])))

arr.sort(key=lambda student: student[1])

for student in arr:
    print(student[0], end=' ')

#lambda 인자: 표현식
y = (lambda x,y : x+y)(12,33)
print(y)

# #map(함수, 리스트)



p = list(map(lambda x: x ** 2, range(5))) 
print(p)

# # Map을 list comprehension으로 구현 
items = [1, 2, 3, 4, 5] 
squared = list(map(lambda x: x**2, items)) 
print(squared)   

squared = [x**2 for x in items] 
print(squared)  

 # Filter를 list comprehension으로 구현 
 
number_list = range(-5, 5) 
less_than_zero = list(filter(lambda x: x < 0, number_list)) 
print(less_than_zero)   
 
less_than_zero = [x for x in number_list if x <0] 
print(less_than_zero)  
