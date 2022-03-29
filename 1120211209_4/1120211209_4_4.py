num = input("请输入一个4位明文:")
a = eval(num[0])
b = eval(num[1])
c = eval(num[2])
d = eval(num[3])
a1 = (a+5)%10
b1 = (b+5)%10
c1 = (c+5)%10
d1 = (d+5)%10
scr = str(c1) + str(d1) + str(a1) + str(b1)
print("密码为：{}".format(scr))