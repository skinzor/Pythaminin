## GithubAPIError ##

class GithubApiError(Exception):
    def __init__(self, status_code):
        if status_code == 403:
            message = 'Rate Limit Was Reached!'
        else:
            message = f'Status Code was: {status_code}'
        super().__init__(message)

raise GithubApiError(69)
