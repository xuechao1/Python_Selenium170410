#coding=utf-8
import  unittest,time
from ecshop.public.method import *
#自动化框架有什么功能才算
#用例模块 写报告 发邮件通知项目组 监控状态  执行用例
#框架就是架构

#在unittest里面写用例的话 必须是test开头
class   Ecshop(unittest.TestCase):
    def setUp(self):  #初始化（前置条件）
        kill_process("firefox")
    def tearDown(self): #恢复环境（用例执行之后的步骤）
        pass
    def test_login_01(self):
        """验证ecshop登录功能"""
        ret=login("http://172.16.3.158/ecshop", "duandongbo", "123456")
        self.assertEqual(ret,True,u"用例执行失败")#断言（判断用例的实际结果跟预期结果是否一致）

    def test2222(self):
        """验证ecshop登录功能222"""
        x=2
        self.assertEqual(x,2,"error")#

    def test3333(self):
        """验证ecshop登录功能333"""
        x=2
        self.assertEqual(x,2,"error")#

    def test4444(self):
        """验证ecshop登录功能444"""
        x=2
        self.assertEqual(x,2,"error")#

if __name__=='__main__':
    unittest.main()