# 문제
# 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데, 1, 3은 남자 2, 4는 여자를 의미한다. 사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.

# >> 주민등록번호: 821010-1635210
# 남자

i = input("주민등록번호를 입력하세요:")

if "1" ==i[7] or "3" ==i[7]:
    print("남자")
else:
    "2" ==i[7] or "4" == i[7]
    print("여자")

# 결과값
# 주민등록번호를 입력하세요 : 898989-3030215
# 여자