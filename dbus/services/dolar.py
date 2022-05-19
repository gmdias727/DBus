from bs4 import *
import requests

def DolarHoje():
    url = 'https://dolarhoje.com/'
    html = requests.get(url)
    
    element = BeautifulSoup(
        html.content, 'html.parser'
    )
    
    return element.find(id='nacional').get('value')