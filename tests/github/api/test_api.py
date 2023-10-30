from src.applications.github.api.github_api import GitHubAPIClient
import requests


def test_search_for_existing_repo():
    github_api_client = GitHubAPIClient()
    existing_repo_name = 'tozend'
    repos = github_api_client.search_repos(existing_repo_name)  # list/array returned

    print('Checking total count is not 0')
    assert repos['total_count'] != 0  # some elements exists in aray/list


def test_search_for_non_existing_repo():
    github_api_client = GitHubAPIClient()
    existing_repo_name = 'jkegojfjcogjercgcjc34tc3crktok'
    repos = github_api_client.search_repos(existing_repo_name)  # list/array returned

    print('Checking total count is 0')
    assert repos['total_count'] == 0  # list of elements is empty
