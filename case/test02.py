import unittest
import requests
from common.logger import Log


class Test_Kuaidi(unittest.TestCase):
    log = Log()
    def setUp(self):
        #测试快递的查询接口
        self.headers = {
            "User-Agent": "Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/69.0.3497.100 Safari/537.36"
        }
    def chaxun_kuaidi(self,danhao,kd,kd_name):
        #三个参数：单号，快递名称（拼音），快递中文名

        self.url = 'http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html'%(danhao,kd)
        self.log.info(u"测试url地址：%s"%self.url)

        #第一步发请求
        r=requests.get(self.url,headers = self.headers)
        result = r.json()
        self.log.info(u"获取请求结果：%s"%result)

        #第二步获取结果
        self.log.info(u"获取公司名称：%s"%result['company'])
        data = result['data'] #获取data里的内容
        self.log.info(u"获取data内容：%s"%result['data'])
        get_result = data[0]['context']#取已签收状态
        self.log.info(u"获取已签收状态：%s"%get_result)

        #断言：测试结果与预期结果的判断
        self.assertEqual(kd_name,result['company'])
        self.assertIn(u"已签收",get_result)

    def test_yuanda(self):
        #测试韵达快递
        self.log.info("-----start------")
        danhao = '3832808463094'
        kd = 'yunda'
        kd_name = u"韵达快递"
        self.log.info(u"测试单号：%s 快递名称：%s"%(danhao,kd_name))
        self.chaxun_kuaidi(danhao,kd,kd_name)
        self.log.info("-----pass-----")

    def test_tiantian(self):
        # 测试韵达快递
        self.log.info("-----start------")
        danhao = '669169041752'
        kd = 'tiantian'
        kd_name = u"天天快递"
        self.log.info(u"测试单号：%s 快递名称：%s" % (danhao, kd_name))
        self.chaxun_kuaidi(danhao, kd, kd_name)
        self.log.info("-----pass-----")

if __name__ == '__main__':  # 建议都加
    unittest.main()
