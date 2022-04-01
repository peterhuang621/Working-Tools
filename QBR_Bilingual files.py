import shutil,os
LC={}
LC['ZH']='zh-CN'
LC['JA']='ja-JP'
LC['KO']='ko-KR'
LC['SV']='sv-SE'
LC['NB']='nb-NO'
LC['DA']='da-DK'
LC['ES']='es-ES'
LC['DE']='de-DE'
LC['FR']='fr-FR'
LC['IT']='it-IT'
LC['PB']='pt-BR'
print(LC)

def copytry(time,prj,languagecode):
	path1='\\\\ec16\\Waters\\EC16\\'+str(time)+'\\'+prj
	path2=path1+'\\9_Deliverable\\FinalDelivery\\Bilingual\\'+languagecode
	x=list(LC.keys())[list(LC.values()).index(lc)]
	path3=path1+'\\0_FromClient\\PM\\'+x+languagecode
	if os.path.exists(path2)==True:
		shutil.copytree(path2,f'C:\\Users\\ECI170\\Desktop\\QBR Q4\\TECH 11\\{languagecode}\\PE\\{prj}')
	elif os.path.exists(path3)==True:
		shutil.copytree(path3,f'C:\\Users\\ECI170\\Desktop\\QBR Q4\\TECH 11\\{languagecode}\\PE\\{prj}')
	elif os.path.exists(path1)==True and os.path.exists(path2)==False and os.path.exists(path3)==False:
		print(languagecode,'|',time,'|',prj)
	else:
		None


filePath0 = r'C:\Users\ECI170\Desktop\QBR Q4'
for lc in LC.values():
	filePath=filePath0+'\\TECH 11\\'+lc+'\\MT'
	for i in os.listdir(filePath):
		copytry(2111,i,lc)




