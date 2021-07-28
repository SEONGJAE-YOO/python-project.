# 완주 여행 키워드 분석
#Step 1. 필요한 모듈을 실행합니다.
from konlpy.tag import *        #pip install konlpy 먼저 하세요 , KoNLPy(코엔엘파이라고 읽는다)는 한국어 정보처리를 위한 파이썬 패키지이다/형태소 분석기 활용하기
import matplotlib.pyplot as plt #pip install matplotlib 먼저 하세요
from matplotlib import font_manager , rc
from wordcloud import WordCloud  # pip install wordcloud 먼저 하세요
from collections import Counter # Counter 클래스 -주어진 단어에서 가장 많이 등장하는 알페벳과 그 알파벳의 개수를 구하는 함수
import nltk #자연어 처리를 위한 파이썬 패키지
okt = Okt()
kkma = Kkma( )
  

#Step 2 . 텍스트 파일을 불러와서 형태소 분석을 합니다.
data1 = open("wanchinpa\완주여행_2017.txt").read( )
data1
  
print(data1)
print("\n")

#Step 3. 키워드를 추출합니다    -Okt 형태소 분석기로 토큰화(1) morphs : 형태소 추출 2) pos : 품사 태깅(Part-of-speech tagging) 3) nouns : 명사 추출)
data2 = okt.nouns(data1) #nonus으로 명사만 추출해준다
#data2 = kkma.nouns(data1)
print("1.추출된 키워드:", data2)
print(len(data2)) #len()은 리스트에 들어있는 원소 개수

# Step 4. 용어 정리 작업하기
data3=[]
for a in data2 :
    if a == "와일드" or a=="축제":
        data3.append(a.replace("와일드","와일드푸드축제"))
    elif a=="로컬" :
        data3.append(a.replace("로컬","로컬푸드"))
    elif a=="메뚜기" :
        data3.append(a.replace("메뚜기","메뚜기구이"))
    elif a=="푸드" :
        data3.append(a.replace("푸드"," "))
    else :
        data3.append(a)
print(data3)

#Step 5. 추출된 단어들의 빈도를 조사한 후 많이 언급된 100개만 출력합니다
print("\n")
data4 = Counter(data3)
data5 = data4.most_common(100)

print("2.단어별 빈도수:",data5)   
# -실행결과
# 2.단어별 빈도수: [('축제', 215), ('완주', 132), ('와일드푸드축제', 122), ('체험', 115), (' ', 97), ('곳', 73), ('블로그', 66), ('아이', 61), ('수', 58), ('물고기', 43), ('먹거리', 40), ('메뚜기구이', 38), ('추억', 34), ('것', 33), ('잡기', 32), ('여행', 30), ('중', 28), ('직 
# 접', 27), ('맛', 27), ('등', 27), ('건', 26), ('정말', 26), ('고산', 25), ('음식', 25), ('셔틀버스', 24), ('시간', 24), ('주소', 23), ('내용', 23), ('구경', 23), ('총', 22), ('데이터', 22), ('수집', 22), ('작성자', 22), ('닉네임', 22), ('작성', 22), ('일자', 22), ('공연', 22), ('개구리', 22), ('튀김', 22), ('거리', 21), ('가을', 21), ('마을', 21), ('구이', 20), ('바로', 20), ('한번', 20), ('처음', 19), ('우리', 19), ('이번', 18), ('내년', 18), ('때', 18), ('마당', 18), ('자연휴양림', 18), ('판매', 17), ('저', 17), ('생각', 17), ('날', 16), ('사람
# ', 16), ('더', 16), ('놀이터', 16), ('지역', 16), ('행사', 15), ('엄마', 15), ('아빠', 15), ('만들기', 15), ('타고', 14), ('요리', 14), ('어른', 14), ('족', 14), ('이용', 14), ('보고', 14), ('문화', 14), ('요', 14), ('인기', 14), ('사진', 13), ('주차', 13), ('옥', 13), ('친구
# ', 13), ('완주군', 13), ('다시', 13), ('꼭', 12), ('저글링', 12), ('대표', 12), ('돼지', 12), ('코', 12), ('제', 12), ('가족', 12), ('또', 12), ('올해', 12), ('전주', 12), ('율', 12), ('하루', 11), ('분', 11), ('좀', 11), ('위', 11), ('프로그램', 11), ('줄', 11), ('부스', 11), ('이', 11), ('현장', 11), ('그', 10)]

#Step 6. 불용어 제거하기 :분석을 하는 것에 있어서는 큰 도움이 되지 않는 단어 제거
sword = open("wanchinpa\와푸gsub.txt").read()
#print(sword)
data6 = [ each_word for each_word in data3
          if each_word not in sword ]
print(data6)

#Step 7. 글자수로 불용어 제거하기
data7 = []
for i in data6 :
    if len(i) >= 2 and len(i) <= 10 :
        data7.append(i) 

print("\n")
print("3.글자수로 불용어 제거" ,data7)

# Step 8. 단어별 빈도수 집계하기
data8 = Counter(data7)
data9 = data8.most_common(50)

print("\n")
print("4.단어별 빈도수 집계하기",data9)
data10 = dict(data9)

# Step 10. 주요 단어들의 빈도를 그래프로 표시하기
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt  #pyplot 모듈의 각각의 함수를 사용해서 그래프를 만들고 변화를 줄 수 있습니다.
import matplotlib 

font_location="wanchinpa\Fonts\H2HDRM.TTF"
font_name=fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font',family=font_name)
plt.figure(figsize=(20,10))

import nltk
from nltk.probability import FreqDist 
    
data11 = FreqDist(data7)  #FreqDist 클래스는 문서에 사용된 단어(토큰)의 사용빈도 정보를 담는 클래스이다.
data11.plot(50)   
             