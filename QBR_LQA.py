import os,shutil

month='2112'
Path=r'\\ec16\\Waters\\EC16\\'+month

for i in os.listdir(Path):
	Path_LQA=f'{Path}\\{i}\\9_Deliverable\\FinalDelivery\\LQA'
	Path_LQA2=f'{Path}\\{i}\\9_Deliverable\\FinalDelivery\\LQA Forms'
	x=month+' '+i
	if os.path.exists(Path_LQA)==True and len(os.listdir(Path_LQA))!=0:
		shutil.copytree(Path_LQA,f'C:\\Users\\ECI170\\Desktop\\QBR Q4\\LQA\\All CJK\\{x}')
	elif os.path.exists(Path_LQA2)==True and len(os.listdir(Path_LQA2))!=0:
		shutil.copytree(Path_LQA2,f'C:\\Users\\ECI170\\Desktop\\QBR Q4\\LQA\\All CJK\\{x}')
	else:
		print(''.join([Path,i]))