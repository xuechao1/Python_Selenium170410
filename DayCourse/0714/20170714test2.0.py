# coding=utf-8
name = ""
age = ""
sal = ""
# 储存增加员工信息的列表
append_list = []
# 储存所有员工信息列表
all_list = []
while 1:
    choose1 = raw_input("""
1、存储员工信息
2、查询员工信息
3、查询所有员工
4、退出
    """)
    if not choose1.isdigit():
        print "输入有误，只能输入1->4数字"
    else:
        choose1 = int(choose1)
        if choose1 == 1:
            print  "存储员工信息"
            while 1:
                # 去掉上一次的新增员工信息
                append_list = []
                name = raw_input("输入姓名")
                if name == "":
                    print "姓名不能为空"
                elif len(name) > 10 or len(name) < 6:
                    print "姓名字符长度为6-10位"
                else:
                    append_list.append(name)
                    # print name
                    break
            while 1:
                age = raw_input("输入年龄")
                if not age.isdigit():
                    print "输入有误，年龄只能为数字"
                else:
                    append_list.append(age)
                    break
            while 1:
                sal = raw_input("输入薪水")
                if not sal.isdigit():
                    print "输入有误，薪水只能为数字"
                else:
                    append_list.append(sal)
                    break
            all_list.append(append_list)
            # print append_list
            # print all_list
        elif choose1 == 2:
            # 判断是否有员工变量
            if name == "":
                print "员工信息为空，请先添加员工信息"
            else:
                print  "查询员工信息"
                # 查询员工信息选项
                while 1:
                    choose2 = raw_input("""可以下3种方式查询员工
                    1、按姓名
                    2、按年龄
                    3、按薪水
                    4、返回菜单首页
                    输入请输入1->4""")
                    if not choose2.isdigit():
                        print "输入有误，只能输入1->3的数字"
                    else:
                        choose2 = int(choose2)
                        if choose2 == 1:
                            print "按姓名查询"
                            while 1:
                                search_name = raw_input("请输入查询员工姓名")
                                count = 0
                                for i in all_list:
                                    if search_name == i[0]:
                                        print "员工姓名:", i[0], \
                                            "员工年龄:", i[1], \
                                            "员工薪水:", i[2]
                                        count += 1
                                if count == 0:
                                    print "员工不存在，请重新输入"
                                break

                        elif choose2 == 2:
                            print "按员工年龄查询"
                            # while 1:
                            #     search_age=raw_input("请输入查询员工年龄")
                            #     if search_age==age:
                            #         print "员工姓名:",append_list[append_list.index(age)-1],\
                            #             "员工年龄:",age,\
                            #             "员工薪水:",append_list[append_list.index(age)+1]
                            #         break
                            #     else:
                            #         print "不存在这个年龄的员工，请重新输入"

                        elif choose2 == 3:
                            print "按员工薪水查询"
                            # while 1:
                            #     search_sal=raw_input("请输入查询员工年龄")
                            #     if search_sal==sal:
                            #         print "员工姓名:",append_list[append_list.index(sal)-2],\
                            #             "员工年龄:",append_list[append_list.index(sal)+1],\
                            #             "员工薪水:",sal
                            #         break
                            #     else:
                            #         print "不存在这个薪水的员工，请重新输入"
                        elif choose2 == 4:
                            print "返回首页成功"
                            break
                        else:
                            print "输入不合法"
        elif choose1 == 3:
            if name == "":
                print "员工信息为空，请先添加员工信息"
            else:
                print  "查询所有员工"
                print "姓名\t" + "年龄\t" + "薪水"
                for i in all_list:
                    for j in i:
                        print j + "\t",
                    print ""
        elif choose1 == 4:
            print  "已成功退出"
            break
        else:
            print "输入不合法，只能输入1->4数字"
