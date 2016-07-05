import concurrent.futures
import json
import requests
import warnings
import csv

warnings.filterwarnings("ignore")


def print_related_info(item):
    print('user_name: ' + item['user']['username'])
    for comment_data in item['comments']['data']:
        print('comment_user_name: ' + comment_data['from']['username'])
    for like_data in item['likes']['data']:
        print('like_user_name: ' + like_data['username'])


def record_related_info(item, layer):
    my_file = open('Instagram_data.csv', 'a', newline='')
    my_writer = csv.writer(my_file)
    for comment_data in item['comments']['data']:
        temp_url = 'http://instagram.com/' + comment_data['from']['username']
        my_writer.writerow([layer, comment_data['from']['username'], temp_url])
    for like_data in item['likes']['data']:
        temp_url = 'http://instagram.com/' + like_data['username']
        my_writer.writerow([layer, like_data['username'], temp_url])
    my_file.close()


class Instagram_Scraper:
    def __init__(self, username):
        self.username = username
        self.numPosts = 0
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)
        self.future_to_item = {}

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
            # self.current_number += 1
            print_related_info(item)
            record_related_info(item, 1)
            # scraper = Instagram_Scraper(item['user']['username'], self.current_number)
            # scraper.media_crawl()
            # self.current_number += scraper.current_number
        if 'more_available' in media and media['more_available'] is True:
            max_id = media['items'][-1]['id']
            self.media_crawl(max_id)


def main():
    field_names = ['Related_layer', 'Username', 'link']
    my_file = open('Instagram_data.csv', 'w', newline='')
    my_writer = csv.writer(my_file)
    my_writer.writerow(field_names)
    my_file.close()
    name = input('Please give me a name to start with: ')
    scraper = Instagram_Scraper(name)
    scraper.media_crawl()


if __name__ == '__main__':
    main()
