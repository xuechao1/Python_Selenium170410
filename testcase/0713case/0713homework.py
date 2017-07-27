# coding=utf-8
"""
1.存储员工信息
2.查询员工信息(查询三种方式name，age，sal)
3.所有员工信息（格式化输出，对齐）
4.退出程序
"""
all = []
choose = 0
choose1 = 0
while 1:
    print """1.存储员工信息  2.查询员工信息  3.打印所有员工信息 4.退出程序"""
    choose = raw_input("欢迎进入客户管理系统请，进行你想要的操作\n")
    if choose == "1":
        name = raw_input("请输入客户名\n")
        all.append(name)
        age = raw_input("请输入年龄\n")
        all.append(age)
        sal = raw_input("请输入薪水\n")
        all.append(sal)
        print "存储客户信息成功\n"
    elif choose == "2":
        print """01、按姓名查询  02、按年龄查询  03、按薪资查询"""
        inputInput = raw_input("请选择你要查询的方式\n")
        if inputInput == "01":
            nameInput = raw_input("请输入您要查询的姓名\n")
            for nameInput in all:
                print nameInput,'\n',
        elif inputInput == "02":
            inputInput = raw_input("请输入您要查询的年龄\n")
            for ageInput in all:
                print ageInput,'\n',
        elif inputInput == "03":
            inputInput = raw_input("请输入您要查询的薪资\n")
            for salInput in all:
                print salInput,'\n',
        else:
            print "请正确选择输入方式\n"
    elif choose == "3":
        for i in all:
            for j in all:
                for x in all:
                    print "%s%d客户信息" % ("共",i*j*x)
    elif choose == "4":

        print "退出成功\n"
    else:
        print "您的操作不符合规范，返回登录界面，请重新操作\n"
