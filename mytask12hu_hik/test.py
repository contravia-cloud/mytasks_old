class Flight:
    class_attr = []
    def __init__(self):
        self.class_attr = []

    def add_instance_att(self, number):
        self.class_attr.append(number)

f= Flight()
g = Flight()
f.add_instance_att(5)

print(f)
    

'''
asdf
192.168.25.2
라우팅
192.168.25.1
DNS
210.220.163.82 219.250.36.130


210.220.163.82 219.250.36.130
'''
