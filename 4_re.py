#정규식
import re  #정규표현식 지원하기 위해 re모듈 사용 /모듈 임포트
           #p =re.compile('정규표현식')을 통해서 정규표현식 컴파일함 
p = re.compile("ca.e")  # . : 하나의 문자를 의미 /care,case 됨 , caffe는 안됨
                       # ^ : 문자열 시작 (^de)이면 desk,destination
                      # $ (se$):문자열 끝 ,case,base 

m= p.match("case") #case가 정규식의 내용가 match(매칭)이 되어 출력됨
print(m.group()) 

# m = p.match("caffe")
# print(m.group()) #매치되지 않으면 에러가 발생

if m:
    print(m.group())
else:
    print("매칭되지 않음")