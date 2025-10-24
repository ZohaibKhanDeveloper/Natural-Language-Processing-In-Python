import spacy
import re
text = """
    Hello! My name is Zohaib khan and My phone number is +92-329-5934563
    and my email is zk510873@gmail.com. Second Phone Number : +92-313-1601520.
    Second Email: zohawordpressdesigner@gmail.com.
    3rd Phone: 03131601520
"""
pattern = '\+\d{2}-\d{3}-\d{7}|\d{11}'
phone = re.findall(pattern,text)
print(phone)
pattern = '[a-z0-9A-Z]*@gmail\.com'
email = re.findall(pattern,text)
print(email)

order = "order[^\d]*(\d+)"
text = """
This is my order # 12345
This is another order 456789
This is  the third order number 101112
"""
order_num = re.findall(order,text)
print(order_num)