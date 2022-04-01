import os
import shutil

a_file = open(r"C:\Users\ECI170\Desktop\Sample.txt","r")
##在桌面建一个Sample.txt放置处理好的Log数据

list_of_lists = []
for line in a_file:
	stripped_line = line.strip()
	list_of_lists.append(stripped_line)
	#将Sample中的每一行作为元素存储（转化为）到列表list_of_lists
a_file.close()

src0=r"D:\Content_Importer\In"
##需要过滤筛选的文件路径
target=r"D:\Content_Importer\finished"
##筛选好文件的目标路径

for i in list_of_lists:
	src=f"{src0}\\{i}"
	#取出各个文件元素并组合到需要过滤筛选的文件路径
	print(src,target)
	#打印下方便追踪错误
	shutil.move(src,target)
	#源路径文件剪切到目标路径