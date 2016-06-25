import gzip
import re
import http.cookiejar
import urllib.request
import urllib.parse


def ungzip(data):
    try:
        print('正在解压……')
        data = gzip.decompress(data)
        print('解压完毕！')
    except:
        print('未经压缩，无需解压')
    return data


def getXSRF(data):
    cer = re.compile('name=\"_xsrf\" value=\"(.*)\"', flags=0)
    strlist = cer.findall(data)
    return strlist[0]


def getOpener(head):
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


headers = {
    'Connection': 'Keep-Alive',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate,br',
    'Host': 'www.zhihu.com',
    'DNT': '1'
}

url = "http://www.zhihu.com/"
req = urllib.request.Request(url, headers=headers)
res = urllib.request.urlopen(req)

data = res.read()
data = ungzip(data)
print(data.decode('utf-8'))
_xsrf = getXSRF(data.decode('utf-8'))

opener = getOpener(headers)

url += 'login/email'
name = 'hzhangal0330@gmail.com'
passwd = 'zhm940330'

postDict = {
    '_xsrf': _xsrf,
    'email': name,
    'password': passwd,
    'remember_me': 'true'
}

postData = urllib.parse.urlencode(postDict).encode()

res = opener.open(url, postData)
data = res.read()

data = ungzip(data)
print(data.decode())
