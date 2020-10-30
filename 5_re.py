#정규식 방법 2
import re  # 정규표현식 지원하기 위해 re모듈 사용 /모듈 임포트
#p =re.compile('정규표현식')을 통해서 정규표현식 컴파일함
p = re.compile("ca.e")  # . : 하나의 문자를 의미 /care,case 됨 , caffe는 안됨
                        # ^ : 문자열 시작 (^de)이면 desk,destination
                        # $ (se$):문자열 끝 ,case,base


def print_match(m):  #함수 사용한 정규식

    if m:
        print("m.group():",m.group()) #일치하는 문자열 반환 
        print("m.string:",m.string) #입력받은 문자열 반환
        print("m.start():",m.start()) # 일치하는 문자열의 시작 index
        print("m.end():",m.end()) #일치하는 문자열의 끝 index
        print("m.span():",m.span()) #일치하는 문자열의 시작 / 끝 index 
    else:   
        print("매칭되지 않음")

# m = p.match("case")  # m을 print_match 함수로 보내줌
# print_match(m)

#1. match 방법
# m = p.match("good case")  # m을 print_match 함수로 보내줌
# print_match(m)           # match:주어진 문자열의 처음부터 일치하는지 확인 해준다
                          # careless는 되고 good case는 매칭되지 않는다
                            
#2. search 방법
m = p.search("good care") #search : 주어진 문자열 중에 일치하는게 있는지 확인한다.
print_match(m)   #care 잘 출력됨

#3. findall 방법
lst = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트로 반환함
print(lst)

#총 정리
#1. p = re.compile("원하는 형태")
#2. m = p.match("비교할 문자열")  : 주어진 문자열의 처음부터 일치하는지 확인    
#3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
#4. lst = p.findall("비교할 문자열"): 일치하는 모든 것을 "리스트" 형태로 반환

#원하는 형태#
# . : 하나의 문자를 의미 /care,case 됨 , caffe는 안됨
# ^ : 문자열 시작 (^de)이면 desk,destination
# $ (se$):문자열 끝 ,case,base