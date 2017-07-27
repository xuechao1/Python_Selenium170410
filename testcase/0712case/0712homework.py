#coding=utf-8
#####################################################作业####################################################
#设计一个系统；注册登录的功能；
#注册的字段（用户名、密码、确认密码） 用户名6-10位；密码6-10位；密码跟确认密码一致，提示用户注册成功
#友好的设计 某个字段输错了 提示用户 让他输对了为止
#登录功能 先注册才能登陆，
#登录用刚刚注册的用户名和密码去登录就行了，如果用户名密码都正确，提示用户登录成功
#登录三次机会，超过三次程序终止运行
while 1:
    print """1.注册  2、登录  3、退出"""
    choose=raw_input("请选择你需要的服务功能\n")
    if choose=='1':
        print "注册功能"
        userName=raw_input("请输入注册用户名\n")
        userPwd=raw_input("请输入注册密码\n")
        ensurePwd=raw_input("请确认注册密码\n")
        if 6<=len(userName)<=10 and 6<=len(userPwd)<=10 and userPwd==ensurePwd:
            print "用户名/密码符合规范,注册成功"
        else:
            print "请检查用户名/密码长度是否符合规范，请重新注册"

    elif choose=='2':
        while 1:
            print "登录功能"
            inputUserName=raw_input("请输入用户名\n")
            inputUserPwd=raw_input("请输入密码\n")
            for login in range(1,4):
                if inputUserName==userName and inputUserPwd==userPwd:
                    print "用户名/密码正确，登录成功"
                elif inputUserName!=userName or inputUserPwd!=userPwd:
                        str="您还有","3-login","次机会"
                        print "用户名/密码错误，请重新登录"
                        print str
                else:
                    if 3-login==0:
                        print "错误次数已达上限，关闭此次登录"
                        break
    elif choose=='3':
        print "选择退出按钮，退出成功"
    else:
        print "请按使用规则选择服务"




