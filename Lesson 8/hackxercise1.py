from urllib.parse import urlparse


def parse_url(url):
    o = urlparse(url)
    return (o.scheme, o.hostname ,o.path)
    
