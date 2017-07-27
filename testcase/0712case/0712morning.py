#coding=utf-8
#计算2的3次方
print 2**3
print "hello world"
#################输出输入############
# raw_input("请输入用户名")
# print 1+2
# print 1+2
# print 1+2
# print 1+2
# print 1+2

x=5
y=2
print 5*2
print 5**2

#1、不能够以数字开头，可以是_或者字母开头，后面可以跟任意字符
# name = raw_input("请输入你的名字")
# print name


##################算数运算####################
print 3+4
print 3-4
print 3*4
print 3/4
print 3//4  #取整    只取小数点前面的
print 3%4   #取余数    取小数点后边的余数
print 3**4  #取次方

##############比较运算################
print 1<2
print 2>3
print 1!=1
print 3==4
print 3.12<=3.12

###########逻辑运算#################and且  or或   not 取反
print 1<2 and 2>3
print 1!=2 or 2>3
print not 2==2
print not 1>2 and 3>1
##############数据类型#############
# int 整型  float浮点型  str字符串  list列表   tuple元组  dict字典
age="23.3"
print type(age)               #查看变量是什么数据类型
print "哈哈"+str(100)
#强制转换 int()   str()   float()
print int("123")
# ' "  """
s="a"
ss='1、增加  2、修改  3、删除'
sss="""aaaa"""
print s
print ss
print sss
#单双引号不能换行，字符只能在一行，三引号可以换行
print """
1、增加
2、修改
3、删除
"""

print "aaa"+"""bbbbb"""   #拼接 连接的意思

x=678
print "个位数是",x%10
print "十位数是",x//10%10
print "百位数是",x//100


y=3254
print "个位数是",y%10
print "十位数是",y//10%10
print "百位数是",y//100%10
print "千位数是",y//1000