
#-*-encoding = utf-8-*-
import jieba  


jieba.load_userdict('wangzhan.txt')
def creadstoplist(stopwordspath):
    stwlist = [line.strip()
               for line in open(stopwordspath, 'r', encoding='utf-8').readlines()]
    return stwlist
stopword = creadstoplist('stopword.txt')
userword = creadstoplist('wangzhan.txt')


f1 =open("content.txt",encoding = 'utf-8')  
f2 =open("fenci_content.txt", 'a',encoding = 'utf-8')  
lines =f1.readlines()  # 读取全部内容 
text = '' 
for line in lines:  
    line.replace('\t', '').replace('\n', '').replace(' ','')  
    seg_list = jieba.cut(line, cut_all=False)
    for word in seg_list:
        if word not in stopword and len(word) > 1 :
            text = str(word) +' '+ text
print(text)		
f2.write(text)	
	#line.replace('\t', '').replace('\n', '').replace(' ','')
	#seg_list = jieba.cut(line, cut_all=False)
	#text = " ".join(seg_list)
	#for word in text:
		#if word not in stopword and len(word)>1 and word in userword:
			#f2.write(word)
	#texts = [[word for word in jieba.lcut(line.strip().replace('\n','').replace('　',''))
		#if word not in stopword and len(word)>1 and word in userword ]]
	#f2.write(" ".join(texts))
#texts = [[word for word in jieba.lcut(" ".join(line).strip().replace('\n','').replace('　',''))
        #if word not in stopword and len(word)>1 and word in userword ]
        #for line in lines]

#f2.write(" ".join(texts))  
f1.close()  
f2.close()