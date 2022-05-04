from distutils.debug import DEBUG
import os
class config:
    NEWS_API_BASE_URL='https://newsapi.org/v2/top-headlines?country=us&apiKey=190cc6c8413944bfa784e6567eafc577'
    NEWS_API_KEY=os.environ.get('190cc6c8413944bfa784e6567eafc577')


class prodconfig(config):
    pass

class DevConfig(config):
    DEBUG = True


config_options={
        'development':DevConfig,
        'production':prodconfig

    }