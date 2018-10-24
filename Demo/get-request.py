import requests
import json

URL = 'https://api.github.com'#主地址

def build_url(endpoint):
    return '/'.join([URL,endpoint])#返回的是字符串。在这用的是字符串的拼接方法

def better_output(json_str):
    return json.dumps(json.loads(json_str),indent=4)#indent = 4表示以第四种方法来显示

def request_method():
    response = requests.get(build_url('users/yinruihua'))#通过.get方法模拟get请求，响应为response里的所有请求
    print(better_output(response.text))
    # print(response.text)
if __name__  == "__main__" :
    request_method()

#status_code 是响应中的状态码
# headers 响应行 application/json 说明返回的是json字符串
# requests.get方法获取他的response

