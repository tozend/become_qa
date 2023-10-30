import os


class Config:
    """Config class is responsible to storing framework's and env's configuration"""

    # EASY
    request_timeout = 29
    user_name = os.environ.get('USERNAME')  # or get if rom elsewhere
    env = os.environ.get('BQA_ENV')


config = Config()

print(config.request_timeout)
print(config.user_name)
print(config.env)