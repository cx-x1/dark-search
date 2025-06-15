import requests
from bs4 import BeautifulSoup
from smart_Ai_agent import RandUserAgent
from termcolor import colored
print(colored(r"""
     .  .
    / `' \
   /(@)(@)\
  /`. \/ .'\
 /   '`'`   \
 |  \'`'`/  |
 |  |'`'`|  |
  \/`'`'`'\/ (PS)
===(((==)))======


""",'light_cyan'))
print(colored('-'*35,'light_yellow'))
print(colored('PLEASE RUN VPN  AND RUN THE CODE','light_red'))
print(colored('-'*35,'light_yellow'))
text = input(colored('text search: ','light_green'))
print(colored('-'*35,'light_yellow'))

headers = {
    'User-Agent': RandUserAgent.get_random_mobile_ua(),
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://ahmia.fi/',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=0, i',
}

params = {
    'q': text,
}

response = requests.get('https://ahmia.fi/search/', params=params, headers=headers)

sub = BeautifulSoup(response.content,'html.parser')
fltrs = sub.find_all('a')
for i, urls in enumerate(fltrs):
    if i >=12:
        print(colored(f'{i} -- {str(urls.get('href')).split('redirect_url=')[-1]}','light_blue'))
print(colored('-'*35,'light_yellow'))
print(colored(f'DONE SEARCH {i} URLS','light_green'))
