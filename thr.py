from concurrent.futures import ThreadPoolExecutor
from Solution import Solution
from AutoAC import AutoAC
import conf
import fun


def main():
	#text = req.get("")
	for i in range(1003,1006):
		s = Solution(i,conf.username,conf.password)
		# todo 多线程！
		#print(s.check())
		a = AutoAC(i)
		code = a.getCode()
		# code = a._getCode("123")
		#print(code)
		s.submit(code)

class App(object):
	#线程池
	def __init__(self,start=1001,end=2000):
		self.start = start
		self.end   = end
		self.pool = ThreadPoolExecutor(conf.poolSize)

	def _start(self,sid):
		#global conf
		fun.msg("Start thread..id:" + str(sid),2)
		s = Solution(sid,conf.username,conf.password)
		a = AutoAC(sid)
		code = a.getCode()
		# code = a._getCode("123")
		#print(code)
		s.submit(code)

	def run(self):
		for i in range(self.start,self.end):
			res = self.pool.submit(self._start,i)
			print(res.result())
		pass
	pass