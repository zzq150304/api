import requests
import unittest
from common.logger import Log


class Test_Login(unittest.TestCase):
    log = Log()
    def login(self,username,password,reme=True):

        url = 'https://passport.womai.com/login/login.do'

        headers = {
            "Accept": "application/json,text/javascript,*/*",
            "Accept-Encoding": "gzip,deflate,br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "164",
            "Content-Type": "application/x-www-form-urlencoded",  # 说明传递的参数是键值对
            "Host": "passport.womai.com",
            "User-Agent": "Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/69.0.3497.100 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }
        json_data = {
            "input1":username,
            "input2":password,
            "remember":reme
        }
        res = requests.post(url,headers = headers,json = json_data,verify = False)
        result1 = res.content#字节输出
        self.log.info('我买网登录时间：%s'%result1)
        return res.json()


    def test_login1(self):
        #u测试登录，正确账号，正确密码
        self.log.info("-----登录成功用例：start!------")
        username = "yinruihua"
        self.log.info("输入正确的账号：%s"%username)
        password = "yinruihua1996"
        self.log.info("输入正确的密码：%s" % password)
        result = self.login(username,password)
        self.log.info("获取测试结果：%s"%result)
        self.assertEqual('2',result['msg'])
        self.log.info("-----pass!------")

    def test_login2(self):
        #u测试登录，正确账号，错误密码
        self.log.info("-----登录失败用例：start!------")
        username = "yinruihua"
        self.log.info("输入正确的账号：%s"%username)
        password = "sdffdgsfdh"
        self.log.info("输入错误的密码：%s"%password)
        result = self.login(username,password)
        self.log.info("获取测试结果：%s"%result)
        self.assertEqual('2',result['msg'])
        self.log.info("-----pass!------")




if __name__ == '__main__':  # 建议都加
    unittest.main()
