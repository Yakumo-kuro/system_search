# !python3
# _*_encoding: utf-8_*_
import os, time
import timeit
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("system_search V2.1")
dt = os.getcwd()
search = None
tm1 = None
tm2 =None
check =None
error=[]
message = '使用說明:\n查檔名輸入:0   檔名前輸入[]不分大小寫 例:[]Chrome\n查時間輸入:1\n路徑範例  :C:\ \n\n有任何問題請聯繫作者:\n作者 :Yakumo\nEmail:ayu2765@gmail.com\n'
print(message)

def deta_check(tm1,tm2):
	while(True):
		if len(str(tm1)) == 14 and len(str(tm2)) == 14:
			check = 1
			break
		else:
			print("輸入錯誤,再次輸入")
			tm1 = int(input("輸入格式(20190101000000): "))
			tm2 = int(input("輸入格式(20191231235959): "))


while(True):
	try:
		i = 0
		l = 0
		e = 0
		print("\n∥查檔名:0∥查時間範圍:1∥不分大小寫:關鍵字前加[]")
		sr = input("輸入0或1: ")
		if sr == str(0):
			dt = input("路徑:")
			search = input("關鍵字:")
		elif sr == str(1):
			dt = input("路徑:")
			tm1 = int(input("輸入格式(20190101000000): "))
			tm2 = int(input("輸入格式(20191231235959): "))
			if check != 1:
				deta_check(tm1,tm2)
		start = timeit.default_timer()
		for dirPath, dirNames, fileNames in os.walk(dt):
			for f in fileNames:
				l+=1
				if sr == str(0):
					if search[:2] == "[]":
						F = f.lower()
						search_l = search[2:].lower()
					else:
						F = f
					if search_l in F:
						try:
							print("┌",os.path.join(dirPath, f))
							status = os.stat(os.path.join(dirPath, f))
							dy = (time.localtime(status[9]))[0]
							dm = (time.localtime(status[9]))[1]
							dd = (time.localtime(status[9]))[2]
							th = (time.localtime(status[9]))[3]
							tm = (time.localtime(status[9]))[4]
							ts = (time.localtime(status[9]))[5]
							print("└─>建立時間:{}-{}-{} {}:{}:{}".format(dy,dm,dd,th,tm,ts))
							i+=1
						except(FileNotFoundError,OSError):
							error.append(os.path.join(dirPath, f))
							e+=1
				elif sr == str(1):
					try:
						status = os.stat(os.path.join(dirPath, f))
						dy = str((time.localtime(status[9]))[0])
						dm = str((time.localtime(status[9]))[1]).zfill(2)
						dd = str((time.localtime(status[9]))[2]).zfill(2)
						th = str((time.localtime(status[9]))[3]).zfill(2)
						tm = str((time.localtime(status[9]))[4]).zfill(2)
						ts = str((time.localtime(status[9]))[5]).zfill(2)
						dtm = int(dy+dm+dd+th+tm+ts)
						if tm2 > dtm > tm1:
							print("┌",os.path.join(dirPath, f))
							print("└─>建立時間:{}-{}-{} {}:{}:{}".format(dy,dm,dd,th,tm,ts))
							i+=1
					except(FileNotFoundError,OSError):
						error.append(os.path.join(dirPath, f))
						e+=1
				else:
					print("Error")
					exit()
		print("\n已在{1}件文件中搜尋到 {0} 件相關資料 {2} 件異常狀況".format(i,l,e))
		end = timeit.default_timer()
		print("用時:{0:.2f}秒\n".format(float(end-start)))
		yn = input("顯示異常(Y/N):")
		if yn == "Y" or yn == "y":
			for li in error:
				print("異常狀況:",li)
		else:
			error.clear()
	except(KeyboardInterrupt, EOFError, SystemExit, TypeError, ValueError):#
		break

