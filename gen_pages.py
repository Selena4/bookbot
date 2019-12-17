import time,io
txt = 'book.txt' #https://convertio.co/ru/pdf-txt/
import codecs
alph = []
nums = []
for num in range(1,100000):
    nums.append(str(num))
for dec in range(65,91):
    alph.append(chr(dec))
for dec in range(97,123):
    alph.append(chr(dec))
fileObj = codecs.open( txt, "r", "utf_8_sig" )
text = fileObj.readlines()
page = ''
page_num = 1
for obj in text:
    obj_to_trans = obj
    boo = True
    while '\n' in obj_to_trans and '\r' in obj_to_trans and ' ' in obj_to_trans:
        obj_to_trans = obj_to_trans.replace('\n','')
        obj_to_trans = obj_to_trans.replace('\r','')
        obj_to_trans = obj_to_trans.replace(' ','')
    for letter in alph:
         if letter in obj_to_trans:
             boo = False
             break
         else:
             continue
    if boo and obj_to_trans in nums:
        file = open('pages/page'+str(page_num)+'.txt','w')
        file.close()
        with io.open('pages/page'+str(page_num)+'.txt', "w", encoding="utf-8") as f:
            f.write(page+'\n'+'Страница: ' + str(page_num))
        page_num += 1
        page = ''
    else:
        page = page + obj
        
    
fileObj.close()
