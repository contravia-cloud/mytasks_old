from selenium import webdriver
from urllib.parse import quote
#from urllib.request import urlopen
from urllib.request import urlretrieve
import os
from bs4 import BeautifulSoup


# 찾고자 하는 검색어를 url로 만들어 준다.
searchterm = 'endmill'

url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="+ quote(searchterm)

# chrom webdriver 사용하여 브라우저를 가져온다.
browser = webdriver.Chrome('./chromedriver')
browser.get(url)

# User-Agent를 통해 봇이 아닌 유저정보라는 것을 위해 사용
header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
# 이미지 카운트 (이미지 저장할 때 사용하기 위해서)
counter = 0
succounter = 0

print(os.path)
# 소스코드가 있는 경로에 '검색어' 폴더가 없으면 만들어준다.(이미지 저장 폴더를 위해서)
if not os.path.exists(searchterm):
    os.mkdir(searchterm)

for _ in range(500):
    # 가로 = 0, 세로 = 10000 픽셀 스크롤한다.
    browser.execute_script("window.scrollBy(0,10000)")
browser.implicitly_wait(1000)
result_soup = BeautifulSoup(browser.page_source, 'html.parser')

'''
result_html = browser.read()

# 개에 대한 태그 정보 찾기
from bs4 import BeautifulSoup

result_soup = BeautifulSoup(result_html,'html.parser')
'''

img_tag = result_soup.find_all("img")
type(img_tag)
print(img_tag)
#image_url = img_tag[10]["data-source"]

# 개 이미지 파일 다운로드

#urlretrieve(image_url, './result/endmill.jpg')

for i in range(0,1000):
    try:
        image_url = img_tag[i]["data-source"]
        urlretrieve(image_url, './result/endmill_{}.jpg'.format(i))
    except Exception as e:
        print(i, end=", ")
        print(e)

print(succounter, "succesfully downloaded")
browser.close()

