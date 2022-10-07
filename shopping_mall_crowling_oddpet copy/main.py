import urllib.request
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen

result = ''

for page in range(1):
        
        webpage = urllib.request.urlopen('https://onnoff.net/board/review/4/')
        soup = BeautifulSoup(webpage, 'html.parser')
        number_pro = soup.find_all('tr','xans-record-') 
        name = soup.find_all('td','thumb left') 
        title = soup.find_all('td','subject left txtBreak') 

        for num in range(15):
                #상품이름
                product_name = name[num].find("span").get_text()
                #상품번호
                product_num = number_pro[num].find("td").get_text().replace(' ','')
                #리뷰 작성자 
                review_person = number_pro[num].find_all("td")[4].get_text().replace(' ','')
                print(review_person)
                #리뷰 제목
                review_title = title[num].get_text().replace('\n','')
                review_detail = title[num].find_all("a")[1]["href"]
                webpage2 = urllib.request.urlopen('https://onnoff.net{}'.format(review_detail))
                soup2 = BeautifulSoup(webpage2, 'html.parser')
               
                if soup2.find('div','detail') != None :
                        #리뷰 내용  
                        review_detail_text = soup2.find('div','detail').get_text().replace(',','@/@').replace('\n','@>@')
                        #리뷰 날짜 
                        review_detail_date = soup2.find('span','txtNum').get_text()     
                        
                #리뷰 이미지 크롤링
                
                if soup2.find('div','detail') != None :
                        review_images = soup2.find('div','detail').find_all("img")
                        number=0
                        for img in review_images:
                                img_Url = img['src']
                                with urlopen('https:'+img_Url) as f:
                                        with open('C:/Users/82108/Desktop/이준명/Data_crowling/shopping_mall_crowling_onnoff/image/img' + "_" + str(product_name.replace(' ','')) + "_" + str(product_num) + "_" + str(number) +'.jpg','wb') as h:
                                                img2 = f.read()
                                                h.write(img2)
                                                number+=1  
                
                result += product_name + ',' + product_num + ',' + review_title + ',' + review_person + ',' + review_detail_date + ',' + review_detail_text + '\n'

f3 = open("./result.csv", 'w', encoding='UTF8')
f3.write(result)
f3.close()       
        
