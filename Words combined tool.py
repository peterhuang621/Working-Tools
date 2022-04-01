#Importing the required packages

from docxcompose.composer import Composer
from docx import Document as Document_compose
import os
import re

TRUEPATH=r'\\ec16\Waters\EC16\2203\22095_Magpie_715006623v02_DESI XS Ion Source OMG CJK\9_Deliverable\To ICR\ko-KR'


def combine_all_docx(PATH):
	files_list=[]
	Names=[]
	for i in os.listdir(PATH):
		files_list.append(os.path.join(PATH,i))
		Names.append(i)
#	print(files_list)
	number_of_sections=len(files_list)
	master = Document_compose()
	composer = Composer(master)
	for i in range(0, number_of_sections):
		masteri = Document_compose()
		masteri.add_heading(Names[i]+'\n',2)
		composer.append(masteri)
		print(i,Names[i])
		doc_temp = Document_compose(files_list[i])
		doc_temp.add_page_break()
		composer.append(doc_temp)
	x=os.path.dirname(PATH)
	y=x+'\\'
	filenames=PATH.replace(y,'')+' combined.docx'
	composer.save(f'{x}\{filenames}')

combine_all_docx(TRUEPATH)