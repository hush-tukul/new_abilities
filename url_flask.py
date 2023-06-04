import datetime

from urllib.parse import urlparse, urlencode, urlunparse




'''-----------------CLASS VERSION-----------------'''
class UTMTracker:
    def __init__(self, url, utm_source, utm_medium, utm_campaign):
        self.url = url
        self.utm_source = utm_source
        self.utm_medium = utm_medium
        self.utm_campaign = utm_campaign
        self.datetime = datetime.datetime.now().strftime('%H:%M:%S-%d/%m/%Y')

    def add_utm_params(self):
        parsed_url = urlparse('http://127.0.0.1:8000')
        query_params = parsed_url.query
        params = {
            'utm_source': self.utm_source,
            'utm_medium': self.utm_medium,
            'utm_campaign': self.utm_campaign,
            'datetime': self.datetime
        }

        # Build the updated URL with UTM parameters
        updated_query_params = urlencode(params)
        updated_url = urlunparse((
            parsed_url.scheme,
            parsed_url.netloc,
            parsed_url.path,
            parsed_url.params,
            updated_query_params,
            parsed_url.fragment
        ))
        print(updated_url)
        return updated_url



redirect_url = UTMTracker('https://t.me/botfatherdev', 'Telegram', 'adv', 'new service').add_utm_params()





