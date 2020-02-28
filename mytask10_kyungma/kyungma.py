import requests
from bs4 import BeautifulSoup

import xml.etree.ElementTree as ET

# 1) reqeusts 라이브러리를 활용한 HTML 페이지 요청
# 1-1) res 객체에 HTML 데이터가 저장되고, res.content로 데이터를 추출할 수 있음
res = requests.get('https://www.garak.co.kr/publicdata/dataOpen.do?id=2697&passwd=Xptmxm100!!&dataid=data4&pagesize=10&pageidx=1&portal.templet=false&p_ymd=20200213&p_jymd=20200212&d_cd=2&p_jjymd=20190213&p_pos_gubun=1&pum_nm=%EA%B7%A4')
xml_data = res.text

# # 2) HTML 페이지 파싱 BeautifulSoup(HTML데이터, 파싱방법)
# # 2-1) BeautifulSoup 파싱방법
soup = BeautifulSoup(xml_data, 'html.parser')

for location in soup.find_all('list'):
    # print(location.findtext("PUM_NM_A"))
    print("품목 = " + location.findtext("PUM_NM_A"))
    


#
# # 3) 필요한 데이터 검색
# title = soup.find("PUM_NM_A")
#
# # 4) 필요한 데이터 추출
# print(title)
#
#
# tree = ET.parse('dataOpen.xml')
# root = tree.getroot()
#
# for child in root.iter("list"):
#     print("품목 = " + child.findtext("PUM_NM_A"))
#     print(child.findtext("PUM_CD"))


#https://www.garak.co.kr/publicdata/dataOpen.do?id=2697&passwd=Xptmxm100!!&dataid=data4&pagesize=10&pageidx=1&portal.templet=false&p_ymd=20200213&p_jymd=20200212&d_cd=2&p_jjymd=20190213&p_pos_gubun=1&pum_nm=귤