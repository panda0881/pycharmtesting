import urllib.request, re, os

target_path = "C:\\Users\\user\\PycharmProjects\\otherFiles"

def save_file(path):
    if not os.path.isdir(target_path):
        os.mkdir(target_path)

    pos = path.rindex('/')
    t = os.path.join(target_path, path[pos + 1:])
    return t


url = "http://www.douban.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/51.0.2704.63 Safari/537.36'}
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request, timeout=2)

data = response.read()

for link, t in set(re.findall(r'(https:[^s]*?(jpg|png|gif))', str(data))):
    print(link)
    try:
        urllib.request.urlretrieve(link, save_file(link))
    except:
        print('fail')
