#for문 예제
for a in["A","B","C"]:
    print(a)

a = [10,20,30]
for i in a:
    print(i)


a = [10,20,30]
for i in a:
    print(i)
    print("_______")

i = "_____"
a = 0 
for a in [1,2,3,4]:
    print("-----")
    if a == 4:
        break

#문제1 
#for 문을 사용해서 리스트에 저장된 값을 다음과 같이 출력하라.

# 리스트 = ["김밥", "라면", "튀김"]
# 오늘의 메뉴: 김밥
# 오늘의 메뉴: 라면
# 오늘의 메뉴: 튀김

a = ["김밥","라면","튀김"]
for i in a:
    print("오늘의 메뉴:"+i)


# 문제2
# 리스트에 주식 종목이름이 저장돼 있다.

# 리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
# 저장된 문자열의 길이를 다음과 같이 출력하라.

# 6
# 4
# 4

list = ["SK하이닉스","삼성전자","LG전자"]
for i in list:
    print(len(i))


# 문제
# 리스트에 동물 이름 저장돼 있다.

# 리스트 = ['dog', 'cat', 'parrot']
# for문을 사용해서 동물 이름의 첫 글자만 출력하라.

# d
# c
# p

list2 = ["dog","cat", "parrot"]
for i in list2:
    print(i[0])

    