# coding=utf-8
# 设计一个系统，注册登录的功能
# 注册的字段（用户名、密码、确认密码）用户名6-10位；密码6-10位；密码跟确认密码一致，提示用户注册成功
# 友好的设计 某个字段输错了，提示用户，让他输对了为止
# 登录功能  先注册才能登录
# 登录用刚刚注册的用户名和密码登录就行了，如果用户名，密码都正确，提示用户登录成功
# 登录三次机会，超过三次程序终止运行

# print 8.0/5
# print 8.0//5
##打印九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print i, "*", j, "=", i * j, '\t',
    print ''
##打印九九乘法表
for i in range(1, 10):
    for j in range(1, i):
        print i, "*", j, "=", i * j, '\t',
    print "\t"
##倒着打印九九乘法表
for i in range(1, 10):
    for j in range(i, 10):
        print i, "*", j, "=", i * j, '\t',
    print ''
