#사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.

# >> input number1: 10
# >> input number2: 9
# >> input number3: 20
# 20

a = int(input("input number1: "))
b = int(input("input number2: "))
c = int(input("input number3: "))

list = [a,b,c]
list.sort(reverse=True) #sort 오름차순 정렬 , reverse 내림차순 정렬 
print(list[0])

#[2,3,4] => 오름차순
#[4,3,2] => 내림차순


