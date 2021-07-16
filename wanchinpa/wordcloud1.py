#Step 1. 필요한 모듈을 실행합니다.
from konlpy.tag import *        #pip install konlpy 먼저 하세요  #konlpy:자바 기반의 형태소 분석기를 파이썬에서 사용할 수 있게 해주는 아주 고마운 라이브러리
import matplotlib.pyplot as plt #pip install matplotlib 먼저 하세요
from matplotlib import font_manager , rc
from wordcloud import WordCloud  # pip install wordcloud 먼저 하세요
from collections import Counter


okt = Okt()
kkma = Kkma( )

#Step 2. 텍스트 파일을 불러와서 형태소 분석을 합니다.
data1 = open("c:\\data\\파이썬_텍스트분석예제_1.txt").read( )
print(data1)
#morphs = 형태소, noun = 명사, pos 형태소 + 품사
#okt() 함수를 이용하여 주요 키워드 추출
print("Kkma:",kkma.nouns("나는 사과, 사과 , 복숭아, 복숭아가 좋아요"))
print("okt:",okt.nouns("나는 사과, 사과 , 복숭아, 복숭아가 좋아요"))

#텍스트 파일을 다시 불러옵니다
data1 = open("c:\\data\\파이썬_텍스트분석예제_1.txt").readlines( )
print(data1)
print("\n")

# 각 줄별로 중복된 단어가 나올 경우 제거하기
data22=[]
for i in data1 :  
        data2=kkma.nouns(i)
        for j in range(0,len(data2)) :
            data22.append(data2[j])
print(data22)

print("\n")
data23 = Counter(data22) 
print("단어별 빈도수:",data23)    #단어별 빈도수: Counter({'나': 3, '사과': 2, '바나나': 1, '복숭아': 1, '단감': 1, '최고': 1, '토마토': 1, '오렌지': 1})

#Step 3. 키워드를 추출하고 빈도를 조사합니다
data1 = open("c:\\data\\파이썬_텍스트분석예제_1.txt").read( )
data2 = okt.nouns(data1)
#data2 = kkma.nouns(data1)
print("1.추출된 키워드:", data2)

print("\n")
data3 = Counter(data2)
print("2.단어별 빈도수:",data3)
  
okt.pos(data1)  

#Step 4. 불용어 제거하기
sword = open("c:\\data\\불용어목록.txt").read()
print(sword)
data4 = [ each_word for each_word in data2
          if each_word not in sword ]
print(data4)

#불용어 -자주 등장하지만 데이터를 분석하는데 있어 큰 의미를 갖지 않는 단어 
#글자수로 불용어 제거하기
data5 = []
for i in data4 :
    if len(i) >= 2 | len(i) <= 10 :
       data5.append(i) 
print(data5)

# Step 5. 단어별 빈도수 집계하기
data6 = Counter(data5)
data7 = data6.most_common(10)
print(data7)
data8 = dict(data7)

# #폰트 검색
# import matplotlib.font_manager as fm

# # 이용 가능한 폰트 중 '고딕'만 선별
# for font in fm.fontManager.ttflist:
#     if 'Gothic' in font.name:
#         print(font.name, font.fname)  


#Step 6. 워드 클라우드 그리기
wordcloud = WordCloud(font_path="C:\Windows\Fonts\H2GTRE.TTF",
                       relative_scaling=0.5,
                       background_color="white"
                     ).generate_from_frequencies(data8)
plt.figure(figsize=(8,4))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()




   
