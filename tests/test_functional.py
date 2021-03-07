import pytest

from main import get_results, get_url_list, get_raw_html
from github_crawler import GithubCrawler
from html_processor import HTMLProcessor

input_values = dict(keywords=[
    'test',
    'python'
], proxies=['68.183.192.29:8080',
            '112.169.9.162:8081',
            '109.172.57.250:23500',
            '105.208.44.183:53480'
            ])
github_crawler = GithubCrawler(input_values['proxies'][0])
html_processor = HTMLProcessor()

wikis_test = None
with open('test_docs/wikis_test.html', 'r') as fr:
    wikis_test = fr.read()


def test_crawl_repositories():

    """
        Test case search repositories on github
    """
    params = input_values
    params['type'] = 'repositories'
    raw = get_raw_html(search_type=params.get('type'),
                       search_keywords=params['keywords'],
                       gh_crawler=github_crawler)
    assert isinstance(raw, str)
    url_list = get_url_list(raw_search_html=raw, search_type=params.get('type'))
    assert isinstance(url_list, list)
    assert len(url_list) > 0
    assert all([isinstance(url, str) for url in url_list])
    results = get_results(url_list=url_list,
                          search_type=params.get('type'),
                          gh_crawler=github_crawler)
    assert isinstance(results, list)
    assert len(results) > 0
    assert all([isinstance(result, dict) for result in results])
    one_result = results[0]
    assert isinstance(one_result['url'], str)
    assert isinstance(one_result['extra'], dict)
    assert isinstance(one_result['extra']['owner'], str)
    assert isinstance(one_result['extra']['language_stats'], dict)

    language_stats = one_result['extra']['language_stats']
    assert round(sum(list(language_stats.values()))) == 100
    assert all([isinstance(language, str) for language in list(language_stats.keys())])


def test_crawl_wikis():

    """
        Test case search wikis on github
    """
    params = input_values
    params['type'] = 'wikis'
    raw = get_raw_html(search_type=params.get('type'),
                       search_keywords=params['keywords'],
                       gh_crawler=github_crawler)
    assert isinstance(raw, str)
    url_list = get_url_list(raw_search_html=raw, search_type=params.get('type'))
    assert isinstance(url_list, list)
    assert len(url_list) > 0
    assert all([isinstance(url, str) for url in url_list])
    results = get_results(url_list=url_list,
                          search_type=params.get('type'),
                          gh_crawler=github_crawler)
    assert isinstance(results, list)
    assert len(results) > 0
    assert all([isinstance(result, dict) for result in results])
    one_result = results[0]
    assert isinstance(one_result['url'], str)


def test_crawl_issues():
    """
        Test case search issues on github
    """
    params = input_values
    params['type'] = 'issues'
    raw = get_raw_html(search_type=params.get('type'),
                       search_keywords=params['keywords'],
                       gh_crawler=github_crawler)
    assert isinstance(raw, str)
    url_list = get_url_list(raw_search_html=raw, search_type=params.get('type'))
    assert isinstance(url_list, list)
    assert len(url_list) > 0
    assert all([isinstance(url, str) for url in url_list])
    results = get_results(url_list=url_list,
                          search_type=params.get('type'),
                          gh_crawler=github_crawler)
    assert isinstance(results, list)
    assert len(results) > 0
    assert all([isinstance(result, dict) for result in results])
    one_result = results[0]
    assert isinstance(one_result['url'], str)
