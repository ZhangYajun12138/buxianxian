#coding = utf-8
import requests
import json
#首页
def main_page():
    response_main_page = requests.get('http://121.40.215.206:8083/pc/doctor/login_one.html')
    return  response_main_page.status_code
    # print(response_main_page.text)

#登陆
def login(s,username,pwd):
    url_login = 'http://121.40.215.206:8083/apis/auth/login'
    headers_login = {'Connection': 'keep-alive',
                    'Content-Length': '133',
                    'Accept': "application/json, text/javascript, */*; q=0.01",
                    'Origin': 'http://121.40.215.206:8083',
                    'X-Requested-With': 'XMLHttpRequest',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                    'Content-Type': 'application/json; charset=UTF-8',
                    'Referer': 'http://121.40.215.206:8083/pc/doctor/login_one.html',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    body_login = json.dumps({"doctorAccount":username,"doctorPwd":pwd})
    r1 = s.post(url=url_login,data=body_login,headers=headers_login)
    return r1.content.decode('utf-8')
    #return r1.json()

#登陆结果分析
def is_login_sucess(res):
    if '100' in res:
        return True
    else:
        return False

if __name__ == '__main__':
    s = requests.session()
    a = login(s,username="zhangyajun",pwd="qvAXDxGM8/xSh6d0rHvl14OxCodzNP/WQghYIp9DbGadJc8DcVjvKhNGSbqcMdaeqm8aKMpQwPjtnmy553xleA==")
    result = is_login_sucess(a)
    print(result)

    b = main_page()
    print(b)