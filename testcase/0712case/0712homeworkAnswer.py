#coding=utf-8
#####################################################作业####################################################
#设计一个系统；注册登录的功能；
#注册的字段（用户名、密码、确认密码） 用户名6-10位；密码6-10位；密码跟确认密码一致，提示用户注册成功
#友好的设计 某个字段输错了 提示用户 让他输对了为止
#登录功能 先注册才能登陆，
#登录用刚刚注册的用户名和密码去登录就行了，如果用户名密码都正确，提示用户登录成功
#登录三次机会，超过三次程序终止运行
choice=0
exit=1
username=""
password=""
errorCount=0
while(exit):
    choice=raw_input("""====================
    请输入选择菜单：
    1.注册
    2.登录
    0.退出
    选择：""")
    if(not choice.isdigit()):
        print("###【ERROR】输入格式有误，请重新输入！###")
    else:
        choice=int(choice)
        if(choice==0):
            exit=0
            print("###系统已退出,感谢您的使用..###")
        elif(choice==1):
            flag1=1
            flag2=1
            while flag1:
                username = raw_input("请输入用户名:(6-10位字符)")
                if(len(username)<6 or len(username)>10):
                    print("###用户名不合法，请重新输入！###")
                else:
                    flag1=0
            while flag2:
                password = raw_input("请输入密码:(6-10位字符)")
                if (len(password) < 6 or len(password) > 10):
                    print("###密码不合法，请重新输入！###")
                else:
                    pass2=raw_input("请重新确认密码:")
                    if(pass2!=password):
                        print("###两次密码输入不一致，请重新设置密码！###")
                    else:
                        flag2=0
            print("###恭喜您！用户%s注册成功！###"%(username))
        elif(choice==2):
            if(len(username)==0):
                print("###您还未注册，请先注册！###")
            else:
                name=raw_input("请输入用户名:")
                passwd=raw_input("请输入密码:")
                if(name!=username or passwd!=password):
                    print("###用户名或密码错误！剩余登录次数:%d###"%(2-errorCount))
                    errorCount+=1
                    if (errorCount > 2):
                        print("###登录次数超限，系统自动退出..###")
                        exit = 0
                else:
                    print("###恭喜您！登录成功..###")
                    errorCount=0
        else:
            print("【ERROR】您的选择有误，请重新输入！")
