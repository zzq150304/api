import requests
import json

URL='https://api.github.com'

def bulid_url(endpoint):
    return '/'.join([URL,endpoint])#主要作用是拼接接口的请求地址

def better_output(json_str):
    return json.dumps(json.loads(json_str),indent=4)#采用json里面提供的方法打印出来，格式更好看

def json_method():
    response=requests.patch(bulid_url('user'),auth=('1677569670@qq.com','yinruihua123456789yinruihua'),json={'company':'haotest','email' : '1677569670@qq.com'})
    print(better_output(response.text))

if __name__ == '__main__':
    json_method()