import requests
import re
import sys
import io
from bs4 import BeautifulSoup
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


#登陆 保持session
#获取题目列表
#查找题目
#提交
#

#提交试题类
#login submit check
#抽象出基类
#try！ catch

class BaseSolution(object):
	def __init__(self,sid,username,password,autosubmit=False):
		self.session = requests.Session()
		self.sid = str(sid)
		login = self._login(username,password)
		print(login)
		pass
	def _login(self,username,password):
		res = self.session.post(self._loginUrl,data = self._loginData)
		if username in res.text:
			return "ok~~~"
		return None
	def submit(self,sid,code):
		pass
	def check(self):
		pass

class Solution(BaseSolution):
	def __init__(self,sid,username,password,autosubmit=False):
		self._loginUrl = "http://acm.hdu.edu.cn/userloginex.php?action=login"
		self._loginData = {"username":username,"userpass":password}
		super().__init__(sid,username,password,autosubmit)
		#http://acm.hdu.edu.cn/userloginex.php?action=login  username   userpass
		pass
	def submit(self,code):
		payload = {}
		payload['problemid'] = str(self.sid)
		payload['language']  = str(2)
		payload['usercode']  = str(code)
		res = self.session.post("http://acm.hdu.edu.cn/submit.php?action=submit",data=payload)
	# def check(self):
	# 	res  = requests.get("http://acm.hdu.edu.cn/status.php?first=&pid=&user=" + self.sid)
	# 	soup = BeautifulSoup(res.text,"html.parser")
	# 	#print(res.text)
	# 	return (soup.table.find_all('tr'))
	pass