# 인터넷 쇼핑몰의 분야별 베스트셀러 상품 크롤러

#Step 1. 필요한 모듈과 라이브러리를 로딩합니다.

from bs4 import BeautifulSoup
from selenium import webdriver
from bitmap import BitMap #많은 픽셀로 정교하고 다양한 색상을 가진 이미지를 만들 수 있다.
                          #이미지 축소와 확대가 가능하지만 이미지가 깨질 수 있고 품질이 떨어진다.
                          #JPG, JPEG, PNG, GIF

import time
import sys
import re
import math
import numpy 
import pandas as pd     
import xlwt  #xlwt는 엑셀 파일을 생성 하고 내용을 작성할 수 있게 해주는 라이브러리
import random
import os

# 학습목표 1 : 사용자에게 다양한 메뉴를 보여 준 후 카테고리값을 입력 받아 해당 카테고리 메뉴를 실행한다.
# Step 2. 사용자에게 카테고리 메뉴를 보여주고 정보를 입력 받습니다.
print("=" *80)
print("     아마존 닷컴의 분야별 Best Seller 상품 정보 추출하기")
print("=" *80)

query_txt='아마존닷컴'
query_url='https://www.amazon.com/bestsellers?ld=NSGoogle'

sec = input('''
    1.Amazon Devices & Accessories     2.Amazon Launchpad            3.Appliances
    4.Apps & Games                     5.Arts, Crafts & Sewing       6.Audible Books & Originals
    7.Automotive                       8.Baby                        9.Beauty & Personal Care      
    10.Books                           11.CDs & Vinyl                12.Camera & Photo             
    13.Cell Phones & Accessories       14.Clothing, Shoes & Jewelry  15.Collectible Currencies       
    16.Computers & Accessories         17.Digital Music              18.Electronics                
    19.Entertainment Collectibles      20.Gift Cards                 21.Grocery & Gourmet Food     
    22.Handmade Products               23.Health & Household         24.Home & Kitchen             
    25.Industrial & Scientific         26.Kindle Store               27.Kitchen & Dining           
    28.Magazine Subscriptions          29.Movies & TV                30.Musical Instruments        
    31.Office Products                 32.Patio, Lawn & Garden       33.Pet Supplies               
    34.Prime Pantry                    35.Smart Home                 36.Software                   
    37.Sports & Outdoors               38.Sports Collectibles        39.Tools & Home Improvement   
    40.Toys & Games                    41.Video Games                

    1.위 분야 중에서 자료를 수집할 분야의 번호를  선택하세요: ''')

cnt = int(input('    2.해당 분야에서 크롤링 할 건수는 몇건입니까?(1-100 건 사이 입력): '))

f_dir = input("    3.파일을 저장할 폴더명만 쓰세요(예:c:\\temp\\):")
print("\n")

if sec == '1' :
      sec_name='Amazon Devices and Accessories'
elif sec =='2' :
      sec_name='Amazon Launchpad'
elif sec =='3' :
      sec_name='Appliances'
elif sec =='4' :
      sec_name='Apps and Games'
elif sec =='5' :
      sec_name='Arts and Crafts and Sewing'
elif sec =='6' :
      sec_name='Audible Books and Originals'        
elif sec =='7' :
      sec_name='Automotive'        
elif sec =='8' :
      sec_name='Baby'
elif sec =='9' :
      sec_name='Beauty and Personal Care'
elif sec =='10' :
      sec_name='Books'
elif sec =='11' :
      sec_name='CDs and Vinyl'
elif sec =='12' :
      sec_name='Camera and Photo'
elif sec =='13' :
      sec_name='Cell Phones and Accessories'
elif sec =='14' :
      sec_name='Clothing and Shoes and Jewelry'
elif sec =='15' :
      sec_name='Collectible Currencies'
elif sec =='16' :
      sec_name='Computers and Accessories'
elif sec =='17' :
      sec_name='Digital Music'
elif sec =='18' :
      sec_name='Electronics'
elif sec =='19' :
      sec_name='Entertainment Collectibles'
elif sec =='20' :
      sec_name='Gift Cards'
elif sec =='21' :
      sec_name='Grocery and Gourmet Food'
elif sec =='22' :
      sec_name='Handmade Products'
elif sec =='23' :
      sec_name='Health and Household'
elif sec =='24' :
      sec_name='Home and Kitchen'
elif sec =='25' :
      sec_name='Industrial and Scientific'
elif sec =='26' :
      sec_name='Kindle Store'
elif sec =='27' :
      sec_name='Kitchen and Dining'
elif sec =='28' :
      sec_name='Magazine Subscriptions'
elif sec =='29' :
      sec_name='Movies and TV'
elif sec =='30' :
      sec_name='Musical Instruments'
elif sec =='31' :
      sec_name='Office Products'
elif sec =='32' :
      sec_name='Patio and Lawn and Garden'
elif sec =='33' :
      sec_name='Pet Supplies'
elif sec =='34' :
      sec_name='Prime Pantry'
elif sec =='35' :
      sec_name='Smart Home'
elif sec =='36' :
      sec_name='Software'
elif sec =='37' :
      sec_name='Sports and Outdoors'
elif sec =='38' :
      sec_name='Sports Collectibles'
elif sec =='39' :
      sec_name='Tools and Home Improvemen'
elif sec =='40' :
      sec_name='Toys and Games'
elif sec =='41' :
      sec_name='Video Games'

if cnt > 30 :
      print("    요청 건수가 많아서 시간이 제법 소요되오니 잠시만 기다려 주세요~~")
else :
      print("    요청하신 데이터를 수집하고 있으니 잠시만 기다려 주세요~~")
      
# Step 3. 저장될 파일위치와 이름을 지정 한 후 크롬 드라이버를 실행하여 페이지를 엽니다
now = time.localtime()
s = '%04d-%02d-%02d-%02d-%02d-%02d' % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
  
os.makedirs(f_dir+s+'-'+query_txt+'-'+sec_name)
os.chdir(f_dir+s+'-'+query_txt+'-'+sec_name)

ff_dir=f_dir+s+'-'+query_txt+'-'+sec_name
ff_name=f_dir+s+'-'+query_txt+'-'+sec_name+'\\'+s+'-'+query_txt+'-'+sec_name+'.txt'
fc_name=f_dir+s+'-'+query_txt+'-'+sec_name+'\\'+s+'-'+query_txt+'-'+sec_name+'.csv'
fx_name=f_dir+s+'-'+query_txt+'-'+sec_name+'\\'+s+'-'+query_txt+'-'+sec_name+'.xls'

s_time = time.time( )

path = "c:/GIT/wanchinpa/driver/chromedriver.exe"
driver = webdriver.Chrome(path)
    
driver.get(query_url)
time.sleep(5)

# 분야별 더보기 버튼을 눌러 페이지를 엽니다
#<ul id="zg_browseRoot">   # xpath으로 찾기 
if sec == '1' : 
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[1]/a""").click( )
elif sec == '2' :                    
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[2]/a""").click( )
elif sec == '3' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[3]/a""").click( )
elif sec == '4' : 
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[4]/a""").click( )
elif sec == '5' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[5]/a""").click( )
elif sec == '6' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[6]/a""").click( )
elif sec == '7' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[7]/a""").click( )  
elif sec == '8' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[8]/a""").click( )
elif sec == '9' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[9]/a""").click( )
elif sec == '10' : 
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[10]/a""").click( )
elif sec == '11' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[11]/a""").click( )
elif sec == '12' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[12]/a""").click( )
elif sec == '13' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[13]/a""").click( )
elif sec == '14' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[14]/a""").click( )
elif sec == '15' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[15]/a""").click( )
elif sec == '16' : 
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[16]/a""").click( )
elif sec == '17' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[17]/a""").click( )
elif sec == '18' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[18]/a""").click( )
elif sec == '19' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[19]/a""").click( )
elif sec == '20' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[20]/a""").click( )
elif sec == '21' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[21]/a""").click( )
elif sec == '22' : 
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[22]/a""").click( )
elif sec == '23' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[23]/a""").click( )
elif sec == '24' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[24]/a""").click( )
elif sec == '25' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[25]/a""").click( )
elif sec == '26' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[26]/a""").click( )
elif sec == '27' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[27]/a""").click( )
elif sec == '28' : 
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[28]/a""").click( )
elif sec == '29' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[29]/a""").click( )
elif sec == '30' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[30]/a""").click( )
elif sec == '31' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[31]/a""").click( )
elif sec == '32' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[32]/a""").click( )
elif sec == '33' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[33]/a""").click( )
elif sec == '34' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[34]/a""").click( )
elif sec == '35' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[35]/a""").click( )
elif sec == '36' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[36]/a""").click( )
elif sec == '37' : 
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[37]/a""").click( )
elif sec == '38' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[38]/a""").click( )
elif sec == '39' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[39]/a""").click( )
elif sec == '40' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[40]/a""").click( )
elif sec == '41' :
      driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[41]/a""").click( )

time.sleep(1)

# 학습목표 2 : 해당 카테고리의 데이터를 수집합니다.
#Step 4. 화면을 스크롤해서 아래로 이동한 후 요청된 데이터를 수집합니다.

def scroll_down(driver):
                                                             #window.scrollTo( X, Y ) 는 왼쪽 상단을 기준(절대위치)으로 하여 스크롤을 이동시키며, window.scrollBy( X, Y ) 는 현재 위치를 기준(상대위치)으로 하여 스크롤을 이동시켜준다는 차이가 있습니다.
      driver.execute_script("window.scrollBy(0,9300);")   #driver.execute_script("window.scrollTo(0, Y)") ,여기서 Y 는 height 을 입력하면 됩니다.
      time.sleep(1)

scroll_down(driver)

# 비트맵 이미지 아이콘을 위한 대체 딕셔너리를 만듭니다 ,Create a dictionary from a sequence of keys
bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
#range으로 fromkeys 설정하기 
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

reple_result = soup.select('#zg-center-div > #zg-ordered-list')
slist = reple_result[0].find_all('li')

if cnt < 51 :
         
    ranking2=[]
    title3=[]
    price2=[]
    score2=[]
    sat_count2=[]
    store2=[]
       
    count = 0

    for li in slist:
            
            f = open(ff_name, 'a',encoding='UTF-8')
            f.write("-----------------------------------------------------"+"\n")

            # 판매순위
            print("-" *70)
            try :
             ranking = li.find('span',class_='zg-badge-text').get_text().replace("#","")
            except AttributeError :
             ranking = ''
             print(ranking.replace("#",""))
            else :
             print("1.판매순위:",ranking)

             f.write('1.판매순위:'+ ranking + "\n")

            #제품 설명 
            try :
             title1 = li.find('div',class_='p13n-sc-truncated').get_text().replace("\n","")
            except AttributeError :
             title1 = ''
             print(title1.replace("\n",""))
             f.write('2.제품소개:'+ title1 + "\n")
            else :
             title2=title1.translate(bmp_map).replace("\n","") 
             print("2.제품소개:", title2.replace("\n",""))
  
             count += 1  
             
             f.write('2.제품소개:'+ title2 + "\n")
            
             # 가격
             try :
               price = li.find('span','p13n-sc-price').get_text().replace("\n","")
             except AttributeError :
               price = ''
               
             print("3.가격:", price.replace("\n",""))
             f.write('3.가격:'+ price + "\n")
                  
             try :
                sat_count = li.find('a','a-size-small a-link-normal').get_text().replace(",","")
             except (IndexError , AttributeError) :  #AttributeError:속성(attribute) 이름이 잘못됐거나 없는 속성을 가져오려 하면 속성 오류(AttributeError)가 발생합니다.
                sat_count='0'
                print('4.상품평 수: ',sat_count)
                f.write('4.상품평 수:'+ sat_count + "\n")
             else :
                print('4.상품평 수:',sat_count)
                f.write('4.상품평 수:'+ sat_count + "\n")

            #상품 별점 구하기
             try :
               score = li.find('span','a-icon-alt').get_text()
             except AttributeError :
               score=' '
               
             print('5.평점:',score)
             f.write('5.평점:'+ score + "\n")

             print("-" *70)
                          
             f.close( )
              
             time.sleep(0.3)
            
             ranking2.append(ranking)
             title3.append(title2.replace("\n",""))
             price2.append(price.replace("\n",""))

             try :   
               sat_count2.append(sat_count)
             except IndexError :
               sat_count2.append(0)

             score2.append(score)

             if count == cnt :
                break
                          
elif cnt >= 51 :    
    
    count = 0
   
    ranking2=[]
    title3=[]
    price2=[]
    score2=[]
    sat_count2=[]
    store2=[]

    for li in slist:           
            f = open(ff_name, 'a',encoding='UTF-8')
            f.write("-----------------------------------------------------"+"\n")

            # 판매순위
            print("-" *70)
            try :
             ranking = li.find('span',class_='zg-badge-text').get_text().replace("#","")
            except AttributeError :
             ranking = ''
             print(ranking.replace("#",""))
            else :
             print("1.판매순위:",ranking)

             f.write('1.판매순위:'+ ranking + "\n")

            #제품 설명 
            try :
             title1 = li.find('div',class_='p13n-sc-truncated').get_text().replace("\n","")
            except AttributeError :
             title1 = ''
             print(title1.replace("\n",""))
             f.write('2.제품소개:'+ title1 + "\n")
            else :
             title2=title1.translate(bmp_map).replace("\n","") 
             print("2.제품소개:", title2.replace("\n",""))

             count += 1
             
             f.write('2.제품소개:'+ title2 + "\n")
            
             # 가격
             try :
               price = li.find('span','p13n-sc-price').get_text().replace("\n","")
             except AttributeError :
               price = ''
               
             print("3.가격:", price.replace("\n",""))
             f.write('3.가격:'+ price + "\n")
                  
             try :
                sat_count = li.find('a','a-size-small a-link-normal').get_text().replace(",","")
             except (IndexError , AttributeError) :
                sat_count='0'
                print('4.상품평 수: ',sat_count)
                f.write('4.상품평 수:'+ sat_count + "\n")
             else :
                print('4.상품평 수:',sat_count)
                f.write('4.상품평 수:'+ sat_count + "\n")

            #상품 별점 구하기
             try :
               score = li.find('span','a-icon-alt').get_text()
             except AttributeError :
               score=' '
               
             print('5.평점:',score)
             f.write('5.평점:'+ score + "\n")

             print("-" *70)
                          
             f.close( )
              
             time.sleep(0.5)

             ranking2.append(ranking)
             title3.append(title2.replace("\n",""))
             price2.append(price.replace("\n",""))

             try :   
               sat_count2.append(sat_count)
             except IndexError :
               sat_count2.append(0)

             score2.append(score)

    # 1 페이지 정보 추출 후 2 페이지로 넘어가기
    driver.find_element_by_xpath("""//*[@id="zg-center-div"]/div[2]/div/ul/li[3]/a""").click( )
    print("\n")
    print("요청하신 데이터의 수량이 많아 다음 페이지의 데이터를 추출 중이오니 잠시만 기다려 주세요~^^")
    print("\n")       
    
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    reple_result = soup.select('#zg-center-div > #zg-ordered-list')
    slist = reple_result[0].find_all('li')
    
    for li in slist:
            
            f = open(ff_name, 'a',encoding='UTF-8')
            f.write("-----------------------------------------------------"+"\n")

            # 판매순위
            print("-" *70)
            try :
             ranking = li.find('span',class_='zg-badge-text').get_text().replace("#","")
            except AttributeError :
             ranking = ''
             print(ranking.replace("#",""))
            else :
             print("1.판매순위:",ranking)

             f.write('1.판매순위:'+ ranking + "\n")

            #제품 설명 
            try :
             title1 = li.find('div',class_='p13n-sc-truncated').get_text().replace("\n","")
            except AttributeError :
             title1 = ''
             print(title1.replace("\n",""))
             f.write('2.제품소개:'+ title1 + "\n")
            else :
             title2=title1.translate(bmp_map).replace("\n","") 
             print("2.제품소개:", title2.replace("\n",""))

             count += 1
             
             f.write('2.제품소개:'+ title2 + "\n")
            
             # 가격
             try :
               price = li.find('span','p13n-sc-price').get_text().replace("\n","")
             except AttributeError :
               price = ''
               
             print("3.가격:", price.replace("\n",""))
             f.write('3.가격:'+ price + "\n")
                  
             try :
                sat_count = li.find('a','a-size-small a-link-normal').get_text().replace(",","")
             except IndexError :
                sat_count='0'
                print('4.상품평 수: ',sat_count)
                f.write('4.상품평 수:'+ sat_count + "\n")
             except AttributeError :
                sat_count='0'
                print('4.상품평 수: ',sat_count)
                f.write('4.상품평 수:'+ sat_count + "\n") 
             else :
                print('4.상품평 수:',sat_count)
                f.write('4.상품평 수:'+ sat_count + "\n")

            #상품 별점 구하기
             try :
               score = li.find('span','a-icon-alt').get_text()
             except AttributeError :
               score=' '
               
             print('5.평점:',score)
             f.write('5.평점:'+ score + "\n")

             print("-" *70)
                         
             f.close( )
              
             time.sleep(0.5)
             
             ranking2.append(ranking)
             title3.append(title2.replace("\n",""))
             price2.append(price.replace("\n",""))

             try :   
               sat_count2.append(sat_count)
             except IndexError :
               sat_count2.append(0)

             score2.append(score)
      
             if count == cnt :
                break
else :
      print(" 검색 건수는 1건 - 최대 100 건까지만 가능합니다")
  

#Step 5. 검색 결과를 다양한 형태로 저장하기
              
amazon_best_seller = pd.DataFrame()
amazon_best_seller['판매순위']=ranking2
amazon_best_seller['제품소개']=pd.Series(title3)
amazon_best_seller['판매가격']=pd.Series(price2)
amazon_best_seller['상품평 갯수']=pd.Series(sat_count2)
amazon_best_seller['상품평점']=pd.Series(score2)


# csv 형태로 저장하기
amazon_best_seller.to_csv(fc_name,encoding="utf-8-sig",index=True)

# 엑셀 형태로 저장하기
amazon_best_seller.to_excel(fx_name ,index=True)

e_time = time.time( )
t_time = e_time - s_time
 
# txt 파일에 크롤링 요약 정보 저장하기
orig_stdout = sys.stdout
f = open(ff_name, 'a',encoding='UTF-8')
sys.stdout = f

# Step 6. 요약 정보를 출력하기
print("\n")
print("=" *50)
print("총 소요시간은 %s 초 이며," %t_time)
print("총 저장 건수는 %s 건 입니다 " %count)
print("=" *50)

sys.stdout = orig_stdout
f.close( )

print("\n") 
print("=" *80)
print("1.요청된 총 %s 건의 리뷰 중에서 실제 크롤링 된 리뷰수는 %s 건입니다" %(cnt,count))
print("2.총 소요시간은 %s 초 입니다 " %round(t_time,1))
print("3.파일 저장 완료: txt 파일명 : %s " %ff_name)
print("4.파일 저장 완료: csv 파일명 : %s " %fc_name)   
print("5.파일 저장 완료: xls 파일명 : %s " %fx_name)
print("=" *80)    