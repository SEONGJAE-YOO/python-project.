
#append() 원소추가
L = []

L.append(1)
L.append(2)
L.append(3)
 
print(L)

# extend() 원소 여러개 추가
L.extend([4,5,6])

print(L)

# sort() 원소 정렬하기 
L = [4,3,15]
L.sort() #reverse=True를 통해 뒤집을 수 있음
print(L)
   
#reverse() 리스트 뒤집기
O = [1,2,3,4,5,6]
O[::3]#처음부터 끝까지 2의 배수 자리 출력
O[::-1]
print(O)
  

#pop() 가장 마지막 원소 제거
L.pop()

#리스트 삭제
L.clear() #생성한 리스트는 남아있지만 내부 항목 모두 삭제

del L #메모리에서 완전히 삭제

##리스트 컴프레헨션 구문 

test_list = [i for i in range(10)]
print(test_list)

#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# if ,else 조건문도 가능 elif 불가
test_list2 = [i if i <4 else 10 for i in range(10)]
print(test_list2)

#[0, 1, 2, 3, 10, 10, 10, 10, 10, 10]

#20에서 30까지 숫자 중 짝수만 리스트에 넣어보자

num = [i for i in range(20,31,2)]
print(num)

# 홀수 1
num = [i for i in range(20,31) if i % 2 ==1 ]
print(num)

#홀수 2
num = [i for i in range(21,31,2)]
print(num)

#짝수 1
num2 = [i for i in range(20,31) if i % 2 == 0]
print(num2)

#짝수 2
num2 = [i for i in range(20,31,2)]
print(num2)

######

L = [ x for x in input("콤마를 기준으로 숫자를 여러개 입력하세요:").split(',')]
print(L)

L = []
for X in input("콤마를 기준으로 숫자를 여러개 입력하세요.:").split(','):
    X = int(X)
    L.append(X)
    print(L)

#콤마를 기준으로 숫자를 여러개 입력하세요.:33,22,11
# [33]
# [33, 22]
# [33, 22, 11]

