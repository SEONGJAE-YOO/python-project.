#Classes and Objects in Python
class Students:

    num_of_students = 0


    def __init__(self,fname,lname,email): #__init__() 함수는 초기화 생성자 또는 초기화메소드/ 인스턴스를 만들때 항상 실행된다는 의미
        self.fname = fname
        self.lname = lname
        self.email = email

        Students.num_of_students += 1

    def fullname(self):
        print(self.fname + ' ' + self.lname)
        
stul = Students('seongjae','yu','yousong4243@naver.com')
print(Students.num_of_students) #1 (실행결과)
stu2 = Students('jonny','sins','sins4243@naver.com')
print(Students.num_of_students)  #2 (실행결과)

Students.fullname(stul)  #seongjae yu (실행결과)

# stul.fullname()
# stu2.fullname()


# print(stul.fname + ' ' + stul.lname)
# print(stu2.fname + ' ' + stu2.lname)
 