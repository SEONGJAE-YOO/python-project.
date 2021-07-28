#def 예제 1

def add(num):
    return num + 4

def ten(num):
    return num * 10

a = add(100)
b = ten(a)
print(b)


# # def 예제 2
def a2(num):
    return num * 2

def b2(num):
    return a2(num + 2)

def c2(num):
    num = num + 10
    return b2(num)

result = c2(2)
print(result)

# def 예제 3 (상속,오버라이딩때 사용 할수 있는 def함수)

class quadriLateral:
    def __init__(self,a,b,c,d):
        self.side1 = a
        self.side2 = b
        self.side3 = c
        self.side4 = d

    def perimeter(self):
        p = self.side1 +self.side2 + self.side3 + self.side4
        print("perimeter=", p)

    
class rectangle(quadriLateral):
    def __init__(self,a,b):
        super().__init__(a,b,a,b)#super() => 자식클래스 에서 부모클래스 메서드 사용하고 싶을때 사용함


r1 = rectangle(10,20)
r1.perimeter()

# 실행값
#perimeter= 60

