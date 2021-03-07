import pytest

from bs4 import BeautifulSoup

from html_processor import HTMLProcessor

html_processor = HTMLProcessor()
"""
    Unit testing for HTMLProcessor
"""


def test_get_owner_name():
    """
    function testing (_get_owner_name) in html_processor
    """
    result = html_processor._get_owner_name(soup=_get_parsed_repo_html())
    assert result == 'reduxjs'


def test_get_params_from_repo_page():
    """
      function testing (get_params_from_repo_page) in html_processor
    """
    results = html_processor.get_params_from_repo_page(repo_html=_get_raw_repo_html())
    assert isinstance(results, dict)
    assert results['owner'] == 'reduxjs'
    assert isinstance(results['language_stats'], dict)
    assert results['language_stats']['JavaScript'] == 100


def test_get_languages_percentage():
    """
      function testing (_get_languages_percentage) in html_processor
    """
    results = html_processor._get_languages_percentage(soup=_get_parsed_repo_html())
    assert isinstance(results, dict)
    assert results['JavaScript'] == 100


def test_get_urls_main_search_repositories():
    """
    Testing function get_urls_main_search
    """
    expected_urls = ['https://github.com/openatx/uiautomator2', 'https://github.com/pytest-dev/pytest',
                     'https://github.com/marmelab/gremlins.js', 'https://github.com/facebook/jest',
                     'https://github.com/binarywang/java-testdata-generator',
                     'https://github.com/travisjeffery/timecop',
                     'https://github.com/session-replay-tools/tcpcopy',
                     'https://github.com/jenkinsci/JenkinsPipelineUnit', 'https://github.com/seattlerb/minitest',
                     'https://github.com/reduxjs/redux-mock-store']

    text = None
    with open('test_docs/test_search_repositories.html', 'r') as fr:
        text = fr.read()

    results = html_processor.get_urls_main_search(main_html=text, search_type='repositories')
    assert isinstance(results, list)
    assert len(results) == 10
    assert results == expected_urls


def test_get_urls_main_search_wikis():
    """
    Testing function get_urls_main_search
    """
    expected_urls = ['https://github.com/br8kpoint/neo4j/wiki/algo', 'https://github.com/hiroller/Theano/wiki/Algo',
                     'https://github.com/liuhu-bigeye/Theano/wiki/Algo', 'https://github.com/HapeMask/Theano/wiki/Algo',
                     'https://github.com/bvandenberghe/Sniffeirb/wiki/algo', 'https://github.com/mxmn/Theano/wiki/Algo',
                     'https://github.com/PtrickH/Theano/wiki/Algo',
                     'https://github.com/CoventryResearch/Theano/wiki/Algo',
                     'https://github.com/dmdigital/Theano/wiki/Algo', 'https://github.com/apjacob/Theano/wiki/Algo']

    with open('test_docs/test_search_wikis.html', 'r') as fr:
        text = fr.read()

    results = html_processor.get_urls_main_search(main_html=text, search_type='wikis')
    assert isinstance(results, list)
    assert len(results) == 10
    assert results == expected_urls


def test_get_urls_main_search_issues():
    """
    Testing function get_urls_main_search
    """
    expected_urls = ['https://github.com/Developer-Student-Clubs-VSSUT-Burla/Master-PyAlgo/issues/5',
                     'https://github.com/KumarAbhinav2/Strings/issues/1',
                     'https://github.com/tryber/sd-03-project-algorithms/pull/35',
                     'https://github.com/equipe-nome-criativo/gc-pratica2/issues/1',
                     'https://github.com/cristobalcifuentes/CHALLENGE-ALKEMY/pull/1',
                     'https://github.com/charankumarpalla/laughing-buddha/pull/108',
                     'https://github.com/carlosprost/SODIIC/issues/1',
                     'https://github.com/Developer-Student-Clubs-VSSUT-Burla/Master-PyAlgo/issues/6',
                     'https://github.com/felixbouveret/find-my-book-back/issues/11',
                     'https://github.com/Kudaraidee/yiimp/issues/13']

    with open('test_docs/test_search_issues.html', 'r') as fr:
        text = fr.read()

    results = html_processor.get_urls_main_search(main_html=text, search_type='issues')
    assert isinstance(results, list)
    assert len(results) == 10
    print(results)
    assert results == expected_urls


def test_get_params_from_repo_page():
    """
    Testing function get_params_from_repo_page for repositories
    """
    with open('test_docs/test_repository.html', 'r') as fr:
        text = fr.read()

    results = html_processor.get_params_from_repo_page(text)
    assert results['owner'] == 'openatx'
    assert results['language_stats']['Python'] == 98.3
    assert results['language_stats']['HTML'] == 1.6
    assert results['language_stats']['Other'] == 0.1


def _get_raw_repo_html():
    text = None
    with open('test_docs/test_repo_page.html', 'r') as fr:
        text = fr.read()
    return text


def _get_parsed_repo_html():
    text = _get_raw_repo_html()
    soup = BeautifulSoup(text, 'html.parser')
    return soup
