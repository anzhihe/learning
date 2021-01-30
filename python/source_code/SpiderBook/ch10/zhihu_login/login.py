#coding:utf-8
# 构造 Request headers
import re
import cPickle
import requests
def get_xsrf(session):
    '''_xsrf 是一个动态变化的参数,从网页中提取'''
    index_url = 'http://www.zhihu.com'
    # 获取登录时需要用到的_xsrf
    index_page = session.get(index_url, headers=headers)
    html = index_page.text
    pattern = r'name="_xsrf" value="(.*?)"'
    # 这里的_xsrf 返回的是一个list
    _xsrf = re.findall(pattern, html)
    return _xsrf[0]

def save_session(session):
# 将session写入文件: session.txt
    with open('session.txt', 'wb') as f:
        cPickle.dump(session.headers, f)
        cPickle.dump(session.cookies.get_dict(), f)
        print '[+] 将session写入文件: session.txt'
def load_session():
    #加载session
    with open('session.txt', 'rb') as f:
        headers = cPickle.load(f)
        cookies = cPickle.load(f)
        return headers,cookies
agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
headers = {
    'User-Agent': agent
}
session = requests.session()
_xsrf = get_xsrf(session)
post_url = 'http://www.zhihu.com/login/phone_num'
postdata = {
            '_xsrf': _xsrf,
            'password': 'xxxxxxxx',
            'remember_me': 'true',
            'phone_num': 'xxxxxxx',
        }
login_page = session.post(post_url, data=postdata, headers=headers)
login_code = login_page.text
print(login_page.status_code)
print(login_code)
save_session(session)


