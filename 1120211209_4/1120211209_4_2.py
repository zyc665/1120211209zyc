wei = eval(input("请输入体重(kg)："))
hei = eval(input("请输入身高(m)："))
bmi = wei / (hei * hei)
print("BMI指数为:{:.2f}".format(bmi))