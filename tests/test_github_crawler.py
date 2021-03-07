import pytest
import requests

from github_crawler import GithubCrawler

"""
    Unit testing for GithubCrawler
"""
gh_crawler = GithubCrawler(proxy='105.208.44.183:53480')


def test_do_request_text():
    """
    Function testing _do_request_text from GithubCrawler
    proxy may need to be updated
    """
    text = gh_crawler._do_request_text('https://google.es')
    assert isinstance(text, str)
    try:
        faulty = gh_crawler._do_request_text("https://idontthinkiexist.tv")
        # Shouldnt be here
    except requests.exceptions.ConnectionError:
        pass


def test_get_relevant_search_url():
    """
    Function testing _get_relevant_search_url from GithubCrawler
    :return:
    """
    type = "issues"
    search_kwords = ['test', 'python']
    url = gh_crawler._get_relevant_search_url(search_type=type, search_keywords=search_kwords)
    assert url == "https://github.com/search?type=issues&q=test+python"
    response = requests.get(url)
    assert response.status_code == 200

