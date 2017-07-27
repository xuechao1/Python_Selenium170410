#coding=utf-8
import unittest,time

#自动化框架有什么功能才算
#用例模块 写报告 发邮件 通知项目组  监控状况  执行用例
#框架就是架构

#在unittest里面 写用例的话 必须是test开头
class Ecshop(unittest.TestCase):
    def setUp(self):  #初始化（前置条件）
        pass
    def tearDown(self):   #恢复环境（用例执行之后的步骤）
        pass
    def test1111(self):
        x=1
        time.sleep(1.5)
        self.assertEqual(x,1,"error")   #断言（判断用例的实际结果跟预期结果是否一致）
    def test2222(self):
        x=5
        time.sleep(1.5)
        self.assertEqual(x,5,"error")   #断言（判断用例的实际结果跟预期结果是否一致）

    def test3333(self):
        x = 77
        time.sleep(1.5)
        self.assertEqual(x, 77, "error")  # 断言（判断用例的实际结果跟预期结果是否一致）

    def test4444(self):
        x = 3
        time.sleep(1.5)
        self.assertEqual(x, 3, "error")  # 断言（判断用例的实际结果跟预期结果是否一致）

    def test5555(self):
        x=2
        self.assertEqual(x,2,"error")  #断言（判断用例的实际结果跟预期结果是否一致）

if __name__=='__main__':
    unittest.main()


