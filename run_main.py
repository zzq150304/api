import unittest
import time
import HTMLTestRunner
import os
#当前脚本所在文件的真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))

def add_case(caseName ='case',rule = 'test*.py'):
    #第一步，加载所有的测试用例
    case_path = os.path.join(cur_path,caseName)
    #如果不存在这个case文件夹，就自动创建一个
    if not os.path.exists(cur_path):os.mkdir(case_path)
    #定义discover方法的参数
    print("test case path:%s"%case_path)
    discover = unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)

    print(discover)
    return discover

def run_case(all_case, reportName="report"):
    #第二步：执行所有的用例，并把结果写入到HTML测试报告中
    #now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path,reportName)#用例文件夹
    #如果不存在这个report文件夹，就自动创建一个
    if not os.path.exists(report_path):os.mkdir(report_path)
    report_abspath = os.path.join(report_path,"result.html")
    print("report path:%s"%report_abspath)
    fp = open(report_abspath,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(fp,title=u"自动化测试报告，测试结果如下：",description=u'用例执行情况')

    #调用add_case函数返回值
    runner.run(all_case)
    fp.close()

if __name__ =="__main__":
    all_case =add_case()#1加载用例
    #生成测试报告的路径
    run_case(all_case)#2.执行用例
