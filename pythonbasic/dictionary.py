# 문제
# 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.

# 번호	통신사
# 011	SKT
# 016	KT
# 019	LGU
# 010	알수없음
# >> 휴대전화 번호 입력: 011-345-1922
# 당신은 SKT 사용자입니다.

num = {"SKT":"011", "KT":"016", "LGU":"019", "알수없음":"010"}
i =input("휴대전화 번호 입력: ").split("-")[0]

if i == num["SKT"]:
    print("당신은 SKT 사용자입니다.")
elif i == num["KT"]:
    print("당신은 KT 사용자입니다.")
elif i == num["LGU"]:
    print("당신은 LGU 사용자입니다.")
else:
    print("당신은 알수없는 사용자입니다.")

# 결과값
# 휴대전화 번호 입력: 016-1234-5678
# 당신은 KT 사용자입니다.