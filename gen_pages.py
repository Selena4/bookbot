import fitz,io,requests,json,time
pdf = 'book.pdf'
doc = fitz.open(pdf)
syms = ['ї']
time.sleep(20)
session = requests.Session()
session.trust_env = False
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
               'Upgrade-Insecure-Requests':'1',
               'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding':'gzip, deflate, br',
               'Connection':'keep-alive',
               'Cache-Control':'no-cache'}
pdf = 'book.pdf'
nums = []
for i in range(1,100):
        nums.append(i)
doc = fitz.open(pdf)
for i in range(len(doc)):
        page = doc[i].getText('text')
        page = page.replace('-\n','52625724215')
        page = page.replace('\n','52625724215')
        req = requests.get('http://api.foxtools.ru/v2/TextDecoder/',headers=headers, params={"text":str(page)})

        if req.status_code != 200 :
                try:
                        with io.open('pages/page'+str(i)+'.txt', "w", encoding="cp1252") as f:
                                f.write(page.replace('52625724215','\n'))
                except:
                        try:
                                with io.open('pages/page'+str(i)+'.txt', "w", encoding="iso-8859-1") as f:
                                        f.write(page.replace('52625724215','\n'))
                        except:
                                with io.open('pages/page'+str(i)+'.txt', "w", encoding="utf-8") as f:
                                        f.write("[Error]")
                                        print('[error] ' + str(i) + ' page')
        else:
                for name in json.loads(req.text)['response']['items']:
                        if name['to']['codePage'] == 1251 and name['to']["displayName"] == "Кириллица (Windows)":
                                file = open('pages/page'+str(i)+'.txt','w')
                                ret = name["value"]
                                ret = ret.replace('52625724215','\n')
                                file.write(ret)
                                break

        file.close()

print('Ready')
