#coding:utf-8
'''
pycurl.HTTP_CODE HTTP ��Ӧ����
'''
import pycurl,StringIO,json,time,re,sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
headers = [
	"User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0",
#	"Accept-Encoding:gzip, deflate",
#	"Accept-Language:zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
#	"Cache-Control:max-age=0",
#	"Connection:keep-alive",
#	"Cookie: city=www; global_cookie=c7ne1g3m0fjmvgs2ipdrsejuk11imfto1wj; __utma=147393320.1067287908.1459400989.1459847155.1459849943.5; __utmz=147393320.1459400989.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); oa_token=157693|n4beV7osgcvqmFudcBkMndGsS2ntM7SQ6C75kjM6c0Sbd3xXC7QqUg%3D%3D; __utmc=147393320; unique_cookie=U_rs8cdhk691pgrej2y0ieyr0lt3mimn2zs6s*19; __utmb=147393320.12.10.1459849943; __utmt_t0=1; __utmt_t1=1",
]
def getHtml(url,headers):
		c = pycurl.Curl()	#ͨ��curl��������һ������
		#c.setopt(pycurl.REFERER, 'http://qy.m.58.com/')	#����referer
		c.setopt(pycurl.FOLLOWLOCATION, True)	#�Զ�������תץȡ
		c.setopt(pycurl.MAXREDIRS,5)			#���������ת���ٴ�
		c.setopt(pycurl.CONNECTTIMEOUT, 60)		#�������ӳ�ʱ
		c.setopt(pycurl.TIMEOUT,120)			#���س�ʱ
		c.setopt(pycurl.ENCODING, 'gzip,deflate')	#����gzip���ݣ���Щɵ����վ���������������û��gzip�������ǻ᷵��һ��gzipѹ�������ҳ
#`		c.setopt(c.PROXY,ip)	# ����
		c.fp = StringIO.StringIO()	
		c.setopt(pycurl.URL, url)	#����Ҫ���ʵ�URL
		c.setopt(pycurl.HTTPHEADER,headers)		#��������ͷ
#		c.setopt(pycurl.POST, 1)
#		c.setopt(pycurl.POSTFIELDS, data)		#����POST����
		c.setopt(c.WRITEFUNCTION, c.fp.write)	#�ص�д���ַ�������
		c.perform()
		code = c.getinfo(c.HTTP_CODE)	#����״̬��
		return code
sum = 1
f=open('result.txt','w')
for line in open('url.txt'):
	url = line.strip()
	http_code = getHtml(url,headers=headers)
	print url+'��%s��url״̬��Ϊ'%sum+str(http_code)
	sum += 1
	f.write(url.strip()+str(http_code)+'\n')
f.close()
#	time.sleep(1)



