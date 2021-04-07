class Universitypeople:
    def __init__(self,fname,lname,email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def fullname(self):
        print(self.fname + ' ' + self.lname)

class Students(Universitypeople):
    pass

class Teachers(Universitypeople):
    def __init__(self,fname,lname,email,salary):
       super().__init__(fname,lname,email) #super()는 부모클래스에서 사용된 함수의 코드를 가져다가 자식 클래스 함수에서 재사용할 때 사용한다
       self.salary = salary

class Maths(Teachers):
    pass


stul = Students('seongjae','yu','yousong4243@naver.com')
stu2 = Students('jonny','sins','sins4243@naver.com')

maths = Teachers('eman','stone','asdds1@naver.com','97000')

print(isinstance(stul,Students)) #isinstance(인스턴스, 클래스/데이터타입)
                                 #식별자가 특정 형의 데이터를 갖고 있는지 확인한다.
                                 #True (실행결과)
print(isinstance(stul,Universitypeople))
print(isinstance(stul,Teachers)) #False (실행결과)

#print(maths.salary) #97000(실행결과)
# stul.fullname() #seongjae yu (실행결과)
# maths.fullname() #eman stone(실행결과)

