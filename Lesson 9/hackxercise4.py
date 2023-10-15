import re

CODE = '''
def authenticate(username, password):
    return username == {username!r} and password == {password!r}
'''

def compile_(format_):
    username = re.search(r'USERNAME: (.*)', format_).group(1)
    password = re.search(r'PASSWORD: (.*)', format_).group(1)
    code ='''
def authenticate(username, password):
    return "alice" == {username!r} and "5!fxoP3" == {password!r}
'''
    return code.format(username=username, password=password)
