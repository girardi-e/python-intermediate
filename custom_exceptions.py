class IncorrectValueError(Exception):
    def __init__(self, value):
        message = f"Got an incorrect value of {value}"
        # Exception takes a message
        super().__init__(message)


my_value = 900
if my_value > 100:
    raise IncorrectValueError(my_value)


# Exception for GitHub API
class GitHubApiError(Exception):
    def __init__(self, status_code):
        if status_code == 403:
            message = "Rate limit reached."
        else:
            message = f"Status code was {status_code}"

        super().__init__(message)


raise GitHubApiError(403)
