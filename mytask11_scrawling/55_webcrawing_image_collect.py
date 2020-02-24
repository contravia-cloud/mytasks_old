from urllib.request import urlopen
from urllib.parse import quote
from urllib.request import urlretrieve

# '개' 검색결과 받기
keyword = "endmill"
url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="+ quote(keyword)
#url = "file:///C:/workspace/myproject/endmill%20_%20네이버%20이미지검색.html"
result = urlopen(url)
print(result)

result_html = result.read()

# 개에 대한 태그 정보 찾기
from bs4 import BeautifulSoup

result_soup = BeautifulSoup(result_html,'html.parser')


img_tag = result_soup.find_all("img")
type(img_tag)
print(img_tag)
#image_url = img_tag[10]["data-source"]

# 개 이미지 파일 다운로드
from urllib.request import urlretrieve

#urlretrieve(image_url, './result/endmill.jpg')

for i in range(0,10):
    try:
        image_url = img_tag[i]["data-source"]
        #image_url = img_tag[i]["src"]
        urlretrieve(image_url, './result/endmill_{}.jpg'.format(i))
    except Exception as e:
        print(i, end=", ")
        print(e)

