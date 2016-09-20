from Solution import Solution
from AutoAC import AutoAC


def main():
	#text = req.get("")
	for i in range(1003,1006):
		s = Solution(i,"201458503124","asdf1234")
		# todo 多线程！
		#print(s.check())
		a = AutoAC(i)
		code = a.getCode()
		# code = a._getCode("123")
		print(code)
		s.submit(code)
if __name__ == '__main__':
	main()