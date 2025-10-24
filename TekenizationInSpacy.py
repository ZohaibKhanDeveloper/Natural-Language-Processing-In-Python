import pandas as pd
import spacy 
nlp = spacy.blank("en")
dataset = pd.read_csv("D:\AI-Project-6th-Semester\datasetCreation\RecomendationSystemDataset.csv")
# print(dataset)
product_names = dataset["Product name"].tolist()
doc = nlp(''.join(product_names[0:]))
token = doc[0]
span = doc[1:5]
print(span)
# for token in doc:
#     print(token)
print(f"Type of DOC : {type(doc)}")
print(f"Type of NLP : {type(nlp)}")
print(f"Type of TOKEN : {type(token)}")
print(f"Type of SPAN : {type(span)}")

text = """
Apple Inc. reported a profit of $5.6 billion in Q1. Meanwhile, Samsung earned €4.2 billion, and Sony generated ¥500 billion in revenue.
The deal between the companies was worth £3 million. Tesla plans to invest ₹200 crore in India. A startup in Dubai secured AED 15 million in funding.
Additionally, a company in Lahore raised PKR 250 million to expand its operations.
"""
doc = nlp(text)
token1 = doc[0]
# print(dir(token1))
for token in doc:
    print(f"""--( TOKEN : {token})-- \n
          IS_ALPHA: {token.is_alpha} \n
          IS_NUM : {token.like_num} \n
          IS_CURRENCY : {token.is_currency}
          """)

text = """
My name is Zohaib khan and i am stdying in BSCS-6TH Semesterin in ICUP.
My Phone Number is : +92 000 0000000.
My Email is : zohaibkhan@gmail.com
My Friend email is : ali@gmail.com
My another friend email is : ayaz123@gmail.com
My another friend email is : imankhalid221364@gmail.com.
"""    
doc = nlp(text)
emails = []
for token in doc:
    if token.like_email:
        emails.append(token)
print(emails)        