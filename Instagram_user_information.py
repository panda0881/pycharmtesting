import concurrent.futures
import json
import requests
import warnings

warnings.filterwarnings("ignore")


def print_related_info(item, number):
    print('media number: ' + str(number))
    print('user_name: ' + item['user']['username'])
    for comment_data in item['comments']['data']:
        print('comment_user_name: ' + comment_data['from']['username'])
    for like_data in item['likes']['data']:
        print('like_user_name: ' + like_data['username'])


class Media_node:
    def __init__(self, name):
        self.name = name
        self.like_num = 0
        self.comment_num = 0


class user_node:
    def __init__(self, name):
        self.name = name
        self.like_num = 0
        self.comment_num = 0


class Instagram_Scraper:
    def __init__(self, username, current_number):
        self.username = username
        self.numPosts = 0
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)
        self.future_to_item = {}
        self.current_number = current_number

    def info_crawl(self):
        url = 'http://instagram.com/' + self.username
        resp = requests.get(url)
        info = json.loads(resp.text)
        print('haha')

    def media_crawl(self, max_id=None):
        """Walks through the user's media"""
        url = 'http://instagram.com/' + self.username + '/media'
        if max_id is not None:
            url += '?&max_id=' + max_id
        resp = requests.get(url)
        media = json.loads(resp.text)
        self.numPosts += len(media['items'])
        if self.numPosts <= 1:
            print('\rFound %i post' % self.numPosts)
        else:
            print('\rFound %i posts' % self.numPosts)
        for item in media['items']:
            self.current_number += 1
            print_related_info(item, self.current_number)
            scraper = Instagram_Scraper(item['user']['username'], self.current_number)
            scraper.media_crawl()
            self.current_number += scraper.current_number
        if 'more_available' in media and media['more_available'] is True:
            max_id = media['items'][-1]['id']
            self.media_crawl(max_id)


def main():
    name = input('Please give me a name to start with: ')
    scraper = Instagram_Scraper(name, 0)
    scraper.media_crawl()


if __name__ == '__main__':
    main()
