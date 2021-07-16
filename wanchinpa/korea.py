# 완주 여행 키워드 분석
#Step 1. 필요한 모듈을 실행합니다.
from konlpy.tag import *        #pip install konlpy 먼저 하세요
import matplotlib.pyplot as plt #pip install matplotlib 먼저 하세요
from matplotlib import font_manager , rc
from wordcloud import WordCloud  # pip install wordcloud 먼저 하세요
from collections import Counter
import nltk #자연어 처리를 위한 파이썬 패키지
okt = Okt()
kkma = Kkma( )
  

#Step 2 . 텍스트 파일을 불러와서 형태소 분석을 합니다.
data1 = open("c:\\data\\완주여행_2017.txt").read( )
data1

print(data1)
print("\n")

#Step 3. 키워드를 추출합니다
data2 = okt.nouns(data1)
#data2 = kkma.nouns(data1)
print("1.추출된 키워드:", data2)
print(len(data2))

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
data5 = data4.most_common(50)

print("2.단어별 빈도수:",data5)

#Step 6. 불용어 제거하기 :분석을 하는 것에 있어서는 큰 도움이 되지 않는 단어 제거
sword = open("c:\\data\\와푸gsub.txt").read()
#print(sword)
data6 = [ each_word for each_word in data3
          if each_word not in sword ]
print(data6)

#Step 7. 글자수로 불용어 제거하기
data7 = []
for i in data6 :  
    if len(i) >= 2 and len(i) <= 10 :
        data7.append(i) 
print(data7)

# Step 8. 단어별 빈도수 집계하기
data8 = Counter(data7)
data9 = data8.most_common(50)
print(data9)
data10 = dict(data9)

    
import numpy as np         # pip install numpy /과학 계산을 위한 라이브러리로서 다차원 배열을 처리하는데 필요한 여러 유용한 기능을 제공
from PIL import Image      # pip install Image
from wordcloud import ImageColorGenerator
korea = np.array(Image.open("c:\data\image\M2jeo.jpg"))  
wc = WordCloud(font_path="C:\Windows\Fonts\H2GTRE.TTF" ,
                       relative_scaling=0.2,mask = korea,
                       background_color="white",
                       min_font_size=1,  
                       max_font_size=50,
                       max_words=500
                     ).generate_from_frequencies(data10)
plt.figure(figsize=(30,20))
plt.imshow(wc)  
plt.axis('off')    
plt.show()     