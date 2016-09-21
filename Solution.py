# -*- coding:utf-8 -*-
#from BaseSolution import BaseSolution
import requests
import re
import sys
import io
from bs4 import BeautifulSoup
import fun
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

		if login == False:
			return
		#print(login)
		pass
	def _login(self,username,password):
		try:
			res = self.session.post(self._loginUrl,data = self._loginData)
		except:
			fun.msg("Login failed..",1)
			return False
		if username in res.text:
			fun.msg("Login success..",0)
			return True
		else:
			fun.msg("Login failed..",1)
			return False
	def submit(self,sid,code):
		pass
	def check(self):
		pass
#登陆 保持session
#获取题目列表
#查找题目
#提交
#

#提交试题类

#多线程

#单元测试


class Solution(BaseSolution):
	def __init__(self,sid,username,password,autosubmit=False):
		#print("asd")
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
		fun.msg("Submit ID:" + payload['problemid'],2)
		try:
			res = self.session.post("http://acm.hdu.edu.cn/submit.php?action=submit",data=payload)
			fun.msg("Submit success..",0)
		except:
			fun.msg("Submit failed..",1)
	# def check(self):
	# 	res  = requests.get("http://acm.hdu.edu.cn/status.php?first=&pid=&user=" + self.sid)
	# 	soup = BeautifulSoup(res.text,"html.parser")
	# 	#print(res.text)
	# 	return (soup.table.find_all('tr'))
	pass