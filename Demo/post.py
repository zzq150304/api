import requests
import unittest

class Test_Login(unittest.TestCase):
    url = 'https://passport.womai.com/login/login.do'

    headers = {
               "Accept":"application/json,text/javascript,*/*",
               "Accept-Encoding":"gzip,deflate,br",
               "Accept-Language":"zh-CN,zh;q=0.9",
               "Connection":"keep-alive",
               "Content-Length":"164",
               "Content-Type":"application/x-www-form-urlencoded",#说明传递的参数是键值对
               "Host":"passport.womai.com",
               "User-Agent":"Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/69.0.3497.100 Safari/537.36",
               "X-Requested-With":"XMLHttpRequest"
    }
    payload = {
        "serverPath":"http://www.womai.com/",
        "loginId":"yinruihua",
        "password":"yinruihua1996",
        "validateCode":"",
        "tempcode":"",
        "mid":"0",
        "returnUrl":"http://www.womai.com/index-0-0.htm"
    }

    def test_login(self):
        response = requests.post(self.url,headers = self.headers,data = self.payload)
        json_data = response.json()
        print(json_data)
        #断言：测试结果与期望结果对比
        self.assertEqual('2',json_data['msg'])


if __name__ =='__main__':#建议都加
    unittest.main()


