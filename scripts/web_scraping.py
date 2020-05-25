
import requests
from bs4 import BeautifulSoup

import sys


class YouTubeClient:

    def get_page(self, url):
        response = requests.get(url)
        return response.text

    def get_page_info(self, html):
        soup = BeautifulSoup(html, features="html.parser")
        # with open('rick.html', 'w') as f:
        #     f.write(html)
        print(soup.head.title.text)
        # result = soup.find(id='eow-description')
        # print(result.text)
        # result = soup.find(id='eow-title')
        # print(result.text)
        # result = soup.find(id='eow-comments')
        # print(result.text)
        # print(html)
        ul = soup.find('ul', {'class': 'watch-extras-section'})
        # print(ul.prettify())
        for li in ul.find_all('li'):
            print(li.a)


def main():
    client = YouTubeClient()
    html = client.get_page('https://www.youtube.com/watch?v=j5a0jTc9S10&list=PLVbxVQf7e2KRz1J34jFf7jDJFDT9lvnQ9')
    client.get_page_info(html)
    # print(sys.getsizeof(html))


if __name__ == "__main__":
    main()

