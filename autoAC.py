import fun
from Solution import Solution
import requests 
import re

#查找代码类
class AutoAC(object):
	def __init__(self,sid,extra=" hdu ",url="blog.csdn.net"):
		self.keyword = str(sid) + extra  + url
		self.url = url
		print(self.keyword)
	def _search(self):
		#https://wap.baidu.com/s?word=1001杭电+ac++site%3Acsdn.net
		res = requests.get("http://cn.bing.com/search?q=" + (self.keyword))
		#print(res.text)
		text = re.findall(r"href=\"(http://" + self.url + ".*?)\"",res.text)
		try:
			fun.msg("Result URL:" + text[0],2)
			return text[0]
		except:
			fun.msg("Fetch result failed..",1)
			return None
	def getCode(self,url=""):
		#功能 
		#优化！
		#url = "http://blog.csdn.net/jopus/article/details/20471117"
		if url == "":
			url = self._search()
		user_agent = {'User-agent': 'Mozilla/5.0'}
		try:
			t = requests.get(url,headers=user_agent)
			code = re.findall(r"#include[.\s\S]*return 0;",t.text)
			code = self._del_tags("".join(code))
			#print(code)
			return code
		except:
			fun.msg("Fetch Code failed..",1)
			return ""
		#1print(t)

	def _del_tags(self,text):
		#功能 ok
		#优化！
		#去掉文字
		text = re.sub(r"<.*?>","",text)
		text = re.sub(r"&lt;","<",text)
		text = re.sub(r"&gt;",">",text)
		text = re.sub(r"&quot;","\"",text)
		text = re.sub(r"&amp;","&",text)
		text = re.sub(r"&nbsp;"," ",text)
		return (text+"\n}")
	pass

