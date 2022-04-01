import pdfplumber
import os

list1= os.listdir(f'C:\\Users\\ECI170\\Desktop\\pdf')
pages=[]

for i in list1:
	filename= str(i)
	file_path = f'C:\\Users\\ECI170\\Desktop\\pdf\\{filename}'
	f=pdfplumber.open(file_path)
	pages.append(len(f.pages))

print(pages)

print(f'total:{sum(pages)}')