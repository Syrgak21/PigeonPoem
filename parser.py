import requests
import textwrap
from bs4 import BeautifulSoup

# Parsing quatians from website

POEM = 'https://emilysuvada.com/extras/the-pigeon-poem'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
full_page = requests.get(POEM, headers=headers)

soup = BeautifulSoup(full_page.content, 'html.parser')
convert = soup.findAll('div', {'class':'et_pb_text_inner'})

zeros = ['A', 'T']
ones = ['C', 'G']


for text in convert:
    content = text.findAll('div')
    if content != []:
        poem = content[0].text 
        for zero in zeros:                               # converting into binary
            poem = poem.replace(zero, '0')
        for one in ones:
            poem = poem.replace(one, '1')
        poem = textwrap.wrap(poem, 8)                    # Dividing into 8-digit parts
        for binary in poem:                              # ASCII convertation
            num = int(binary, 2)
            print(chr(num), end='')
