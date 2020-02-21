import xml.etree.ElementTree as ET

tree = ET.parse('dataOpen.xml')
root = tree.getroot()
print(root)
for child in root:
    print(child.tag, child.attrib)

#http://www.garak.co.kr/publicdata/dataOpen.do?id=2697&passwd=Xptmxm100!!&dataid=data4&pagesize=10&pageidx=1&portal.templet=false&p_ymd=20200213&p_jymd=20200212&d_cd=2&p_jjymd=20190213&p_pos_gubun=1&pum_nm=귤