import urllib.request


def save_file(content):
    path = "C:\\Users\\user\\PycharmProjects\\pycharmtesting\\testing.out"
    f = open(path, 'wb')
    f.write(content)
    f.close()


url = "http://www.douban.com"

request = urllib.request.Request(url)

response = urllib.request.urlopen(request)

data = response.read()

save_file(data)

data = data.decode('utf-8')

print(data)
print(type(response))
print(response.geturl())
print(response.info())
print(response.getcode())
