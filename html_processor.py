from typing import Optional
from bs4 import BeautifulSoup


class HTMLProcessor:
    """
    This class is used to process raw HTML and find relevant info
    """
    base_url = 'https://github.com'
    main_html = None

    def get_urls_main_search(self, main_html: str, search_type: str) -> list:
        """
        :param search_type: str flagging the type of element we are looking for
        :return: a list with collected urls
        """
        if search_type == 'repositories':
            return self._get_repositories_urls(main_html)
        elif search_type == 'issues':
            return self._get_issues_urls(main_html)
        elif search_type == 'wikis':
            return self._get_wikis_urls(main_html)

    def _get_issues_urls(self, main_html: str) -> list:
        """
        :return: list with urls
        """
        results = []
        soup = BeautifulSoup(main_html, 'html.parser')
        upper_div = soup.find('div', id='issue_search_results')
        for lower_div in upper_div.findAll('div', class_='f4 text-normal'):
            for a in lower_div.findAll('a'):
                if not a or not a.get('href'):
                    continue
                results.append(f'{self.base_url}{a.get("href")}')
        return results

    def _get_wikis_urls(self, main_html: str) -> list:
        """
        :return: list with urls
        """
        results = []
        soup = BeautifulSoup(main_html, 'html.parser')
        upper_div = soup.find('div', id='wiki_search_results')
        for lower_div in upper_div.findAll('div', class_='f4 text-normal'):
            for a in lower_div.findAll('a'):
                if not a or not a.get('href'):
                    continue
                results.append(f'{self.base_url}{a.get("href")}')
        return results

    def _get_repositories_urls(self, main_html: str) -> list:
        """
        :return: list with urls
        """
        results = []
        soup = BeautifulSoup(main_html, 'html.parser')
        ul = soup.find('ul', class_='repo-list')
        for li in ul.findAll('li', class_='repo-list-item'):
            a = li.find('a', class_='v-align-middle')
            if not a or not a.get('href'):
                continue
            results.append(f'{self.base_url}{a.get("href")}')
        return results

    def get_params_from_repo_page(self, repo_html: str) -> dict:
        """
        :param repo_html: HTML in str format
        :return: a dict with the params
        """
        soup = BeautifulSoup(repo_html, 'html.parser')
        owner_name = self._get_owner_name(soup=soup) or 'Unknown'
        language_percentages = self._get_languages_percentage(soup=soup)
        return {'owner': owner_name,
                'language_stats': language_percentages
                }

    @staticmethod
    def _get_owner_name(soup: BeautifulSoup) -> Optional[str]:
        """
        :param soup: raw HTML from the repository
        :return: a str with the name of the owner
        """
        owner_as = soup.findAll('a', class_='url fn')
        if len(owner_as) != 1:
            return None
        owner_a = owner_as[0]
        name = owner_a.text
        return name

    @staticmethod
    def _get_languages_percentage(soup: BeautifulSoup) -> Optional[dict]:
        """
        :param soup: raw HTML from the repository
        :return: a dict containing the languages used and % of usage
        """
        results = {}
        for s in soup.findAll('span', class_='Progress-item'):
            if s.get('aria-label'):
                language, percentage = s['aria-label'].split(' ')
                results[language] = float(percentage)
        return results
