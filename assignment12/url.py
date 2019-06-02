# Feedback:
#
#     + Nice solution!
#     + Cool use of union to avoid having to share state between coroutines.
#       (Though it's not hard to do.)
#     - Hashbang missing.
#
# Sorry it took so long (again). Good luck with the exam.

import urllib, urllib.request
from multiprocessing import Pool, cpu_count
from datetime import datetime
from os.path import basename, splitext, join


def download_images(*urls):
    pool = Pool(cpu_count())  # number of concurrent processes can be limited here

    img_urls = pool.map_async(get_img_urls, urls).get()
    img_urls = set().union(*img_urls)  # union of lists

    print('Images to be downloaded:', img_urls)

    pool.map_async(download_image, img_urls).get()


def download_image(img_url):
    name, extension = splitext(basename(img_url))
    file_name = join('imgs', f'{name}_{datetime.now().strftime("%Y-%m-%d_%H:%M:%S:%f")}{extension}')
    print(f'Downloading image {img_url} -> {file_name}')
    urllib.request.urlretrieve(img_url, file_name)


def get_img_urls(doc_url):
    from html.parser import HTMLParser
    from urllib.parse import urljoin

    class ImgUrlParser(HTMLParser):
        def error(self, message):
            print('Error:', message)

        def __init__(self):
            HTMLParser.__init__(self)
            self.output_list = []

        def handle_starttag(self, tag, attrs):
            nonlocal doc_url

            if tag == 'img':
                src_attr = dict(attrs).get('src')
                url = urljoin(doc_url, src_attr)
                self.output_list.append(url)

    print(f'Downloading content from {doc_url}')
    content = urllib.request.urlopen(doc_url).read().decode('utf-8')
    parser = ImgUrlParser()
    parser.feed(content)
    return parser.output_list


if __name__ == '__main__':  # test the implementation
    download_images('http://stackoverflow.com/', 'https://www.mff.cuni.cz/en', 'https://www.mff.cuni.cz/')
