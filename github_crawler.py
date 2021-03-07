import requests
import time

from exceptions import CrawlerValidationException, Not200Exception


class GithubCrawler:
    """
    This class will handle the requests to Github using proxies and will return HTML
    code for the required search
    """
    allowed_types = ('repositories', 'issues', 'wikis')
    base_url = 'https://github.com/search'

    search_keywords = []
    type = None
    proxy_dict = None
    repo_url = None


    def __init__(self, proxy: str = None):
        if proxy:
            self.proxy = {
                'https': f"http://{proxy}",
                'http': f"http://{proxy}"
            }
        else:
            raise CrawlerValidationException('Crawling parameters are not valid')

    def get_search_html_from_github(self, search_type: str, search_keywords: list) -> str:
        # Build the URL with given params
        url = self._get_relevant_search_url(search_type, search_keywords)
        # Query github & get the HTML
        return self._do_request_text(url)

    def get_repo_html(self, url: str) -> str:
        # Requests individual repo HTML
        return self._do_request_text(url)

    def _get_relevant_search_url(self, search_type: str, search_keywords: list) -> str:
        """
        :param search_type: Param for search
        :param search_keywords: Terms to be searched on Github
        :return: Suitable url that matches the criteria
        """
        url = f"{self.base_url}?type={search_type}&q={'+'.join(search_keywords)}"
        return url

    def _do_request_text(self, url: str) -> str:
        """
        :param url: The url to query
        :return: Str containing the requested HTML
        """
        # Returns the raw html from the url passed as arg
        response = requests.get(url=url,)# proxies=self.proxy)
        if response.status_code == 200:
            # Stop to avoid being banned
            time.sleep(0.7)
            return response.text
        else:
            raise Not200Exception(f'Status code {response.status_code} in {response.url}')
