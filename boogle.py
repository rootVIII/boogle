from argparse import ArgumentParser
from datetime import datetime
from json import dump
from sys import exit
from src.news_scraper import NewsScraper


if __name__ == '__main__':
    description = 'Scrape Google News'
    parser = ArgumentParser(description=description)
    parser.add_argument('-p', '--path', required=True,
                        help='path to chromedriver bin/exe')
    parser.add_argument('-x', '--headless', required=False, action='store_true',
                        help='run in terminal only (no GUI)')
    args = parser.parse_args()

    if args.headless:
        print('Running headless...')
        client = NewsScraper(args.path, headless=True if args.headless else False)
    else:
        print('Running normally...')
        client = NewsScraper(args.path)

    try:
        client.run_news_bot()
    except Exception as err:
        print('Fatal error encountered while locating Google links:')
        print(err)
        exit(1)
    finally:
        client.close_browser()

    try:
        articles = client.find_image_links()
        file_name = datetime.now().strftime('%Y%m%d%H%M%S')
        with open(f'result-{file_name}.txt', 'w') as file_out:
            dump(articles, file_out, indent=4)
    except Exception as err:
        print('Fatal error encountered while scraping found links:')
        print(err)
        exit(1)
