import requests


class GitHubAPIClient:
    """Current class contains every API call we use in tests"""

    def __init__(self):
        pass

    def search_repos(self, repo_name):
        print('Sending request to url https://api.github.com/search/repositories')
        r = requests.get("https://api.github.com/search/repositories", params={'q': repo_name})

        body = r.json()
        print(f'Responce retreived {body}')

        return body

    def search_commits(self, commit_hash):
        print('Sending request to url https://api.github.com/search/commits')
        r = requests.get("https://api.github.com/search/commits", params={'q': commit_hash})

        body = r.json()
        print(f'Responce retreived {body}')

        return body
