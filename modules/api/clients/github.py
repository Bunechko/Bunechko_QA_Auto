import requests


class GitHub:

    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": name}
        )
        body = r.json()

        return body

    def statistics(self, owner, repo):
        r = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}/stats/contributors"
        )
        body = r.json()

        return body
    
    def repository_subscribers(self, owner, repo):
        r = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}/subscribers",
        )
        body = r.json()

        return body
    
    def repo_subscribers_count(self, owner, repo):
        r = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}",
        )
        body = r.json()

        return body
