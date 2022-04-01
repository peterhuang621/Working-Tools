import pdfplumber
from openpyxl import Workbook

book= Workbook()
sheet = book.active
#创建一个新的EXCEL表以便统计

filename= 'ECI_Invoice_USLX20220300039.pdf'
#PDF的名字
path=r'\\ec16\Waters\EC16\2203\Quote\Invoice'
#PDF所在的路径
file_path = f'{path}\\{filename}'

pdf=pdfplumber.open(file_path)
#用pdfplumber加载打开PDF
pn=len(pdf.pages)
print(pn)
#统计PDF的页数并打印

def etables(x):
	pdf=pdfplumber.open(file_path)
	page_table=pdf.pages[x].extract_tables()
	#第i页的表格提取出来
	tn=0
	sheet.append([f'page {x+1}'])
	#在每一页前加个是第几页的提示page(i+1)，i起始为0但是我们的起始页为1
	if tn<len(page_table):
		table=page_table[tn]
		for list1 in table:
			sheet.append(list1)
		tn+=1
		#以上将提取的表格分裂成行，逐个加在空行处

for i in range(pn):
	etables(i)
	#对PDF每一页进行提取

book.save(f'{path}\\{filename}.xlsx')
#将表格存放到同一处，同一名的EXCEL文档中
