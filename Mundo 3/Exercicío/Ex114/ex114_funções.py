"""
Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""


def site(url):
    import requests
    try:
        n = requests.get(url)
    except requests.exceptions.ConnectionError:
        print(f'O site {url} não está acessível')
    else:
        print(f'O site {url} está acessível')
