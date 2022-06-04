while 1:
	password=input("请输入密码:")
	if len(password)<6:
         print("长度为6位，请重试")
	 continue
	if password=="123456":
         print("恭喜你，密码正确")

	else:
	 	print("密码有误，请重试")
