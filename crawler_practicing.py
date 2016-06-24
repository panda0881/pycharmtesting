import urllib.request


def save_file(content):
    path = "C:\\Users\\user\\PycharmProjects\\pycharmtesting\\testing.out"
    f = open(path, 'wb')
    f.write(content)
    f.close()


url = "http://www.douban.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/51.0.2704.63 Safari/537.36'}
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request, timeout=2)

data = response.read()

save_file(data)

data = data.decode('utf-8')

print(data)
print(type(response))
print(response.geturl())
print(response.info())
print(response.getcode())
