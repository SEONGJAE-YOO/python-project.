# Inheritance
class Students:

    num_of_students = 0


    def __init__(self,fname,lname,email): #__init__() 함수는 초기화 생성자 또는 초기화메소드/ 인스턴스를 만들때 항상 실행된다는 의미
        self.fname = fname
        self.lname = lname
        self.email = email

        Students.num_of_students += 1

    def fullname(self):
        print(self.fname + ' ' + self.lname)

class Teachers(Students):
    pass        
        
stul = Students('seongjae','yu','yousong4243@naver.com')
stu2 = Students('jonny','sins','sins4243@naver.com')

maths = Teachers('eman','stone','asdds1@naver.com')

print(maths.fname)
maths.fullname()

Students.fullname(stul)  #seongjae yu (실행결과)
print(Students.num_of_students)
# stul.fullname()
# stu2.fullname()


# print(stul.fname + ' ' + stul.lname)
# print(stu2.fname + ' ' + stu2.lname)
 