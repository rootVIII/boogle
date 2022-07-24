from random import random, randint
from re import search
from time import sleep

# 3rd party libs
from requests import get
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By


class NewsScraper:
    def __init__(self, chromedriver_path, headless=False):
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--log-level=3')

        if headless:
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('-disable-gpu')
            chrome_options.add_argument('--window-size=1920,1080')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')

        self.browser = Chrome(chromedriver_path, options=chrome_options)
        self.browser.set_page_load_timeout(30)

        google = 'https://news.google.com/topics/'
        self.sections = {
            'US':
                f'{google}CAAqIggKIhxDQkFTRHdvSkwyMHZNRGxqTjNjd0VnSmxiaWdBUAE',
            'World':
                f'{google}CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB',
            'Business':
                f'{google}CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pWVXlnQVAB',
            'Technology':
                f'{google}CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB',
            'Entertainment':
                f'{google}CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pWVXlnQVAB',
            'Sports':
                f'{google}CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pWVXlnQVAB',
            'Science':
                f'{google}CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pWVXlnQVAB',
            'Health':
                f'{google}CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ'
        }

        self.articles = {key: [] for key in self.sections}

    @staticmethod
    def scrape_og_img(html):
        for line in html.split('<'):
            if 'meta' in line:
                if '\"og:image\"' in line or '\'og:image\'' in line:
                    break
                if '\"og:image:url\"' in line:
                    break
        else:
            raise Exception(f'Failed to find og:image')

        og_pattern = r'\s?content\W+(\S+)\W?\s?'

        og_link = search(og_pattern, line).group(1).strip().replace('\"', '')
        og_link = og_link.replace('>', '')
        if 'https://' not in og_link:
            raise Exception('OG Link does not contain https://')

        if og_link[-1] == '/':
            og_link = og_link[:-1]

        return og_link

    def find_image_links(self):
        for section, article_details in self.articles.items():
            for index, article in enumerate(article_details):
                try:
                    req = get(article['link'], timeout=30, allow_redirects=True)
                    # Get the actual URL and replace Google's 302 redirect URL
                    self.articles[section][index]['link'] = req.url
                    self.articles[section][index]['image_link'] = self.scrape_og_img(req.text)
                except Exception as err:
                    self.articles[section][index]['image_link'] = str(err)

        return self.articles

    def get_anchor_tags(self):
        for tag in self.browser.find_elements(By.TAG_NAME, 'a'):
            tag_text = tag.text.strip().replace('\n', ' ')
            yield tag_text, tag.get_attribute('href')

    def run_news_section(self, section, url):
        self.browser.get(url)
        sleep(randint(8, 13) + random())

        for title, href in self.get_anchor_tags():
            if not title or len(title.split()) < 5 or not href:
                continue
            if 'google.com/publications' in href:
                continue

            self.articles[section].append({
                'title': title, 'link': href, 'image_link': ''
            })

    def run_news_bot(self):
        for news_section, link in self.sections.items():
            self.run_news_section(news_section, link)

    def close_browser(self):
        self.browser.close()
