#coding=utf-8
"""
1.存储员工信息
2.查询员工信息（查询三种方式name,age,sal）
3.所有员工信息（格式化输出，对齐）
4.退出程序
"""
choice=0
exit=1
all=[]
list1=[]
while(exit):
    choice=raw_input("""=============================
    请输入选择菜单：
    1.存储员工信息
    2.查询员工信息
    3.所有员工信息
    4.退出程序
    选择：""")
    if choice == "1":
        "存储员工信息"
        name = raw_input("请输入该员工的姓名：")
        # list1.append(name)
        sex = raw_input("请输入该员工的性别：")
        # list1.append(sex)
        salary=raw_input("请输入该员工的薪资：")
        # list1.append(salary)
        #print list1
        all.append([name,sex,salary])
        #print all
    elif choice=="2":
        "查询员工信息"
        query = raw_input("""+++++++++++++++++++++++++++++++++++++++
            请输入您的条件：
                01.按姓名查询
                02.按年龄查询
                03.按薪资查询
                     """)
        if query=="01":
            "按姓名查询"
            name2=raw_input("请输入查询的姓名：")
            print "姓名\t年龄\t薪资\t"
            for i in all:
                if name2 ==i[0]:
                    print i[0],"\t",i[1],"\t",i[2]
            print i, len(all)
            if i == len(all):
                print "没有该姓名"
        elif query=="02":
            "按年龄查询"
            sex = raw_input("请输入查询的年龄：")
            print "姓名\t年龄\t薪资\t"
            for i in all:
                if sex ==i[0]:
                    print i[0],"\t",i[1],"\t",i[2]
            print i, len(all)
            if i==len(all):
                print "没有该年龄"
        elif query=="03":
            "按薪资查询"
            salary = raw_input("请输入查询的薪资：")
            print "姓名\t年龄\t薪资\t"
            for i in all:
                if salary ==i[0]:
                    print i[0],"\t",i[1],"\t",i[2]
            print "没有该薪资"
    elif choice=="3":
        "所有员工信息"
        print "姓名\t年龄\t薪资\t"
        for i in range(0, len(all)):
            for j in range(0,3):
                print all[i][j],"\t",
            print ""
    elif choice=="4":
        "退出程序"
        break
    else:
        print "没有该选项，请重新输入"
