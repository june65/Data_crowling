import urllib.request
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen

result = ''
number_pit = 1

for page in range(1,5):
        
        webpage = urllib.request.urlopen('https://p-hiti.com/board/review/list.html?board_no=4&page={}'.format(page))
        soup = BeautifulSoup(webpage, 'html.parser')
        number_pro = soup.find_all('li','box xans-record-')
        
        for num in number_pro:
                #상품이름
                product_name = num.find('div',"product-name").get_text().replace(',','@/@').replace('\n','@>@')
                #상품번호
                product_num = number_pit
                #리뷰 작성자 
                review_person = num.find('div',"writer").get_text().replace('\n','')
                #리뷰 제목
                review_title = num.find('div','subject').get_text().replace(',','@/@').replace('\n','@>@')
                #리뷰 날짜 
                review_detail_date = num.find('div','date').get_text().replace(',','@/@').replace('\n','@>@')
                #리뷰 내용  
                review_detail_text = num.find('div','content').get_text().replace(',','@/@').replace('\n','@>@')
                print(review_detail_text)
                number_pit += 1
                #리뷰 이미지 크롤링
                
                if num.find('div','product-thumb') != None :
                        review_images = num.find('div','product-thumb').find_all("img")
                        number=0
                        print(review_images)
                        for img in review_images:
                                img_Url = img['src']
                                
                                with urlopen('https:'+img_Url) as f:
                                        with open('C:/Users/82108/Desktop/이준명/Data_crowling/shopping_mall_crowling_phiti/image/img' + "_" + str(product_name.replace(' ','')) + "_" + str(product_num) + "_" + str(number) +'.jpg','wb') as h:
                                                img2 = f.read()
                                                h.write(img2)
                                                number+=1  
                
                result += product_name + ',' + str(product_num) + ',' + review_title + ',' + review_person + ',' + review_detail_date + ',' + review_detail_text + '\n'
        ''' 
        name = soup.find_all('td','thumb left') 
        title = soup.find_all('td','subject left txtBreak') 
        for num in range(15):
                
                webpage2 = urllib.request.urlopen('https://onnoff.net{}'.format(review_detail))
                soup2 = BeautifulSoup(webpage2, 'html.parser')
               
                if soup2.find('div','detail') != None :
                        
                        #리뷰 날짜 
                        review_detail_date = soup2.find('span','txtNum').get_text()     
                 
                
        
f3 = open("./result.csv", 'wt', encoding='UTF8')
f3.write(result)
f3.close()    
'''  