#coding:utf-8
'''
pycurl.HTTP_CODE HTTP 响应代码
'''
import pycurl,StringIO,json,time,re,sys,urllib2
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
		c = pycurl.Curl()	#通过curl方法构造一个对象
		#c.setopt(pycurl.REFERER, 'http://qy.m.58.com/')	#设置referer
		c.setopt(pycurl.FOLLOWLOCATION, True)	#自动进行跳转抓取
		c.setopt(pycurl.MAXREDIRS,3)			#设置最多跳转多少次
		c.setopt(pycurl.CONNECTTIMEOUT, 60)		#设置链接超时
		c.setopt(pycurl.TIMEOUT,120)			#下载超时
		c.setopt(pycurl.ENCODING, 'gzip,deflate')	#处理gzip内容，有些傻逼网站，就算你给的请求没有gzip，它还是会返回一个gzip压缩后的网页
#`		c.setopt(c.PROXY,ip)	# 代理
		c.fp = StringIO.StringIO()	
		c.setopt(pycurl.URL, url)	#设置要访问的URL
		c.setopt(pycurl.HTTPHEADER,headers)		#传入请求头
#		c.setopt(pycurl.POST, 1)
#		c.setopt(pycurl.POSTFIELDS, data)		#传入POST数据
		c.setopt(c.WRITEFUNCTION, c.fp.write)	#回调写入字符串缓存
		c.perform()
		code = c.getinfo(c.HTTP_CODE)	#返回状态码
		return code
sum = 0
for line in open('url.txt'):
	sum += 1
print '共有%s条url'%sum
f=open('result.txt',r'a')
for line in open('url.txt'):
	url = line
	http_code = getHtml(url,headers=headers)
	if http_code==200:
		html = urllib2.urlopen(url).read()
		result = re.findall(r'rtright',html)
		num = 0
		for line in result:
			num += 1
		if num == 1:
			print url+'状态码为:'+str(http_code)+'该帖子没有回复！'
			f.write(url.strip()+' '+str(0)+'\n')
		elif num > 1 and num < 10:
			num = num - 1		
			print url+'状态码为:'+str(http_code)+'回复数:'+str(num)
			f.write(url.strip()+' '+str(num)+'\n')
		elif num == 10:	
			num = num - 1
			print url+'状态码为:'+str(http_code)+'回复数大于或等于:'+str(9)
			f.write(url.strip()+' '+str(num)+'\n')
	else:
		print url+'状态码为:'+str(http_code)
		f_404=open('404.txt',r'a')
		f_404.write(url)
		f_404.close()
f.close()
#	time.sleep(1)



