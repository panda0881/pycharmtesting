import concurrent.futures
import json
import requests
import warnings

warnings.filterwarnings("ignore")


def related_info(item):
    print('user_name: ' + item['user']['username'])
    for comment_data in item['comments']['data']:
        print('comment_user_name: ' + comment_data['from']['username'])
    for like_data in item['likes']['data']:
        print('like_user_name: ' + like_data['username'])


class Instagram_User_Scraper:
    def __init__(self, username):
        self.username = username
        self.numPosts = 0
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)
        self.future_to_item = {}

    def crawl(self, max_id=None):
        """Walks through the user's media"""
        url = 'http://instagram.com/' + self.username + '/media'
        if max_id is not None:
            url += '?&max_id=' + max_id
        resp = requests.get(url)
        # resp = urllib.request.Request(url=url)
        media = json.loads(resp.text)
        self.numPosts += len(media['items'])
        if self.numPosts <= 1:
            print('\rFound %i post' % self.numPosts)
        else:
            print('\rFound %i posts' % self.numPosts)

        for item in media['items']:
            related_info(item)

        if 'more_available' in media and media['more_available'] is True:
            max_id = media['items'][-1]['id']
            self.crawl(max_id)


class Instagram_Hashtag_Scraper:
    def __init__(self, username):
        self.username = username
        self.numPosts = 0
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)
        self.future_to_item = {}

    def crawl(self, max_id=None):
        """Walks through the user's media"""
        url = 'http://instagram.com/' + self.username + '/media'
        if max_id is not None:
            url += '?&max_id=' + max_id
        resp = requests.get(url)
        # resp = urllib.request.Request(url=url)
        media = json.loads(resp.text)
        self.numPosts += len(media['items'])
        if self.numPosts <= 1:
            print('\rFound %i post' % self.numPosts)
        else:
            print('\rFound %i posts' % self.numPosts)

        for item in media['items']:
            related_info(item)

        if 'more_available' in media and media['more_available'] is True:
            max_id = media['items'][-1]['id']
            self.crawl(max_id)


def main():
    choice = input('Which one do you want to start with? user or hashtag?')
    if choice == 'user' or choice == 'User':
        name = input('Please give your start user-name: ')
        scraper = Instagram_User_Scraper(name)
        scraper.crawl()
    elif choice == 'hashtag' or choice == 'Hashtag':
        name = input('Please give your start hashtag-name: ')
        scraper = Instagram_Hashtag_Scraper(name)
        scraper.crawl()


if __name__ == '__main__':
    main()
