import random
from github_crawler import GithubCrawler
from html_processor import HTMLProcessor

# Place the input values here
input_values = dict(keywords=[
    'css', 'nova'
], proxies=['68.183.192.29:8080',
            '112.169.9.162:8081',
            '109.172.57.250:23500',
            '105.208.44.183:53480'
            ], type='Issues')

html_processor = HTMLProcessor()


def start_scraping(input_values: dict):
    search_keywords = input_values['keywords']
    search_type = input_values['type'].lower()
    proxies = input_values['proxies']
    proxy = proxies[random.randint(0, len(proxies)) - 1]

    # Create Crawler with proxy params
    gh_crawler = GithubCrawler(proxy=proxy)

    # Get raw HTML from Github search page and process it to find repo URLs
    raw_search_html = get_raw_html(search_type=search_type,
                                   search_keywords=search_keywords,
                                   gh_crawler=gh_crawler)
    # At this point, we have all the URLs show matching the criteria
    url_list = get_url_list(raw_search_html=raw_search_html, search_type=search_type)
    results = get_results(url_list=url_list, search_type=search_type, gh_crawler=gh_crawler)
    return results


def get_raw_html(search_type: str, search_keywords: list, gh_crawler: GithubCrawler):
    return gh_crawler.get_search_html_from_github(search_type=search_type,
                                                  search_keywords=search_keywords)


def get_url_list(raw_search_html: str, search_type: str):
    return html_processor.get_urls_main_search(main_html=raw_search_html,
                                               search_type=search_type)


def get_results(url_list: list, search_type: str, gh_crawler: GithubCrawler):
    results = []
    if search_type == 'repositories':
        for repo_url in url_list:
            raw_repo_html = gh_crawler.get_repo_html(repo_url)
            results.append({'url': repo_url,
                            'extra': html_processor.get_params_from_repo_page(raw_repo_html)
                            })
    else:
        results = [{'url': url} for url in url_list]

    return results


print(start_scraping(input_values=input_values))
