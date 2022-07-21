import urllib.request
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen

for page in range(1,12):

        webpage = urllib.request.urlopen('https://fashiondog.kr/product/list.html?cate_no=27&page={}'.format(page))
        soup = BeautifulSoup(webpage, 'html.parser')
        name = soup.find('ul','prdList grid4')
        boxes = soup.find_all(attrs={'id':re.compile('^anchorBoxId\_')})
        for box in boxes:
                product_name = box.find("strong","name")
                product_id = box["id"].replace("anchorBoxId_", '')

                #상세페이지 들어가기
                webpage2 = urllib.request.urlopen('https://fashiondog.kr/product/1/{}/'.format(product_id))
                soup2 = BeautifulSoup(webpage2, 'html.parser')
                
                #상품 이름 + 가격
                product_name2 = soup2.find("div","product_title")
                product_price = box.find("span","strike")

                #사진 번호
                num = 1

                #메인 이미지 저장
                main_image = soup2.find("img","BigImage") 
                img_Url = main_image['src']
                with urlopen('https:'+img_Url) as f:
                        with open('./image/img'+ str(product_id) + "_" +str(num) +'.jpg','wb') as h:
                                img2 = f.read()
                                h.write(img2)
                num+=1

                print(product_name2.get_text(), product_price.get_text())
                #옵션 출력하기
                tbody_color = soup2.find_all("tbody","xans-element- xans-product xans-product-option xans-record-")[0]
                tbody_size = soup2.find_all("tbody","xans-element- xans-product xans-product-option xans-record-")[1]

                option_color = tbody_color.find_all("option")
                option_size = tbody_size.find_all("option")
                
                for i in range(2,len(option_color)):
                       print(option_color[i]["value"])
                for i in range(2,len(option_size)):
                       print(option_size[i]["value"])

                #상세 이미지 저장
                detail_image_box = soup2.find("div","cont")
                detail_image = detail_image_box.find_all("img")
                for img in detail_image:
                        img_Url = img['ec-data-src']
                        with urlopen('https://fashiondog.kr'+img_Url) as f:
                                with open('./image/img'+ str(product_id) + "_" +str(num) +'.jpg','wb') as h:
                                        img2 = f.read()
                                        h.write(img2)
                        num+=1