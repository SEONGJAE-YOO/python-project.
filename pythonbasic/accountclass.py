# 문제
# 은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정됩니다. Account 클래스를 생성한 후 생성자를 구현해보세요. 생성자에서는 예금주와 초기 잔액만 입력 받습니다. 은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.

# 은행이름: SC은행
# 계좌번호: 111-11-111111

import random

class Account:
    def __init__(self,name,balance): #생성자와 같은 역할
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)

        num1 = str(num1).zfill(3) #0으로 채울때 zfill함수 사용함
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number  = num1 + '-' + num2 + '-' + num3

yu = Account("유성재", 100000000000)
print("성함 :",yu.name)
print("잔액 :",yu.balance)
print("은행이름 :",yu.bank)
print("계좌번호 :",yu.account_number)
  
# 출력결과

# 성함 : 유성재
# 잔액 : 100000000000
# 은행이름 : SC은행
# 계좌번호 : 527-76-357448




# 1-1) Class는 무엇?

# * (Class와 Object)의 관계는 (과자틀과 과자)의 관계라고 이해하면 쉽다

#    - Class : 똑같은 무엇인가를 계속 만들어낼 수 있는 설계 도면 같은 것(과자틀)

#    - Object: Class에 의해서 만들어진 피조물(과자)
# [출처] [Python] Class와 __init__ 이해|작성자 N or N



# 파이썬에서 __init__ 함수는 자바에서 생성자와 비슷한 역할을 한다. 즉, 한 객체에 대한 인스턴스를 생성할 때 호출되는 것이 __init__ 함수라고 보면 되겠다.

 

# 다음은 Car 클래스를 생성하고, 이 클래스에 대한 __init__ 함수를 정의한 후 인스턴스를 생성하면 어떻게 결과가 나타나는지를 보여주기 위한 예제 코드이다.

 

# class Car:
#     def __init__(self, brand):
#         self.brand = brand
#         print(brand + " 한 대가 생성되었습니다.")
        
        
# c = Car("벤츠")


# 출처: https://marshallslee.tistory.com/entry/파이썬에서-init-함수는-어떤-역할을-하는가 [Astronaut's Note]