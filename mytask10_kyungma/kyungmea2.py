import requests
from xml.etree import ElementTree

# URL="http://www.garak.co.kr/publicdata/dataOpen.do?id=2697&passwd=Xptmxm100!!&dataid=data4&pagesize=10&pageidx=1&portal.templet=false&p_ymd=20200213&p_jymd=20200212&d_cd=2&p_jjymd=20190213&p_pos_gubun=1&pum_nm=귤"
URL="http://www.garak.co.kr/publicdata/dataOpen.do"
params = {'id': '2697',
          'passwd': 'Xptmxm100!!',
          'dataid': 'data4',
          'pagesize': '10',
          'pageidx': '1',
          'portal.templet' : 'false',
          'p_ymd': '20200214',
          'p_jymd': '20200212',
          'd_cd': '2',
          'p_jjymd': '20190213',
          'p_pos_gubun': '1',
          'pum_nm': '귤'}
# params.setdefault('f', 100)
# print(params)

res = requests.get(URL, params=params)
tree = ElementTree.fromstring(res.content)
# tree = elemTree.parse('./dataOpen.xml')

f = open("./data_list.txt", 'a')
for list_tag in tree.findall('./list'):
    child_tags = list_tag.findall('*')
    data = ''
    for child_tag in child_tags:
        data = data + '\t' + child_tag.text
    data = data + '\n'
    f.write(data)
f.write('\n')
f.close()






    # grade_tag = list_tag.find('G_NAME_A')
    # unit_tag = list_tag.find('U_NAME')
    # if grade_tag.text == '상' and unit_tag.text == '   3키로상자':
    #     print(grade_tag.text)
    #     avr_price_tag = list_tag.find('AV_P_A')
    #     print(avr_price_tag.text)


