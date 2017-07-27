#coding=utf-8
########################################作业#######################
# 在昨天的程序基础上修改
# 增加功能 5.修改（根据id 修改年龄、修改薪水）   6.删除（根据id删除该用户的所有信息）
# 增加的时候 添加一个字段id，在做增加用户的时候做判断，判断id不能重复；
# 整个代码功能都在文件中实现，用户增加 删除  改 查 都是在文件里
def reg():
    while 1:
        name = raw_input("请输入名字：")
        passwd = raw_input("请输入密码：")
        passwd2 = raw_input("请输入确认密码")
        age = raw_input("请输入年龄")
        sal = raw_input("请输入薪水")
        reg_data = name + '\t' + passwd + '\n'
        ret = write_file("data.txt", reg_data)
        print add_userId(filename,userId)
        print ret
def write_file(filename, data):
    try:
        fileobj = open(filename, "a")
        fileobj.write(data)
        fileobj.close()
        return "数据写入文件成功"
    except:
        return "数据写入文件失败"
def read_file(filename):
    try:
        fileobj = open(filename, "r")
        data = fileobj.readlines()
        fileobj.close()
        return data
    except:
        data = []
        return data
def login(username, passwd):
    user_data = read_file('data.txt')
    count = 0
    for user in user_data:
        user = user.replace("\n", "")
        user_list = user.split("\t")
        if username == user_list[0] and passwd == user_list[1]:
            count += 1
    if count != 0:
        return "登录成功"
    else:
        return "登录失败"
while 1:
    choose = raw_input("1.注册  2.登录")
    if choose == '1':
        reg()
    elif choose == '2':
        username = raw_input("请输入用户名：")
        passwd = raw_input("请输入密码：")
        ret = login(username, passwd)
        print ret
    else:
        print "无该选项"
def add_userId(filename,userId):
    filename = reg(filename)
    userId = reg(filename)[3]+len(username)[2]+len(passwd)[1]+len(passwd)[0]
    print userId
del reg(filename),add_userId(userId)


