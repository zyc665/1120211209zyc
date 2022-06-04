import random
games = 10
for i in range(games):
	print("进行第{}场游戏".format(i+1))

	feeling = random.randint(0,10)#0:开心，1:不爽，2:愤怒
	if 5<= feeling <= 9:
		print("中断本次游戏，开始下一局")
		continue
	elif feeling == 10:
		print("中断游戏，不玩了")
		break
	else:
		print("玩得很开心")
	result = random.randint(0,1) #0:失败，1:胜利
	if result == 1:#获胜
		print("朋友圈炫耀战绩")
	else: #result ==O,失败
		print("沉默...")
	print("*"*20)
