### step 0
# Install all the requirements
import requests
from bs4 import BeautifulSoup
# Choose any random website to scrap its content
url = "https://pypi.org/" 

### step 1: Get the HTML
content = requests.get(url)
htmlcontent = content.content
"""print(htmlcontent) """


### step 2: Parse the HTML
soup = BeautifulSoup(htmlcontent, 'html.parser')
"""print(soup.prettify)"""


### step 3 : HTML tree traversal
title = soup.title
"""print(title)                  # 1.Tag """
"""print(type(soup))             # 2.BeautifulSoup """
"""print(type(title.string))     # 3.Navigable String """


### step 4 : BrautifulSoup
# Get all the paragraphs from the page
paras = soup.find_all('p')
"""print(paras)"""

# Get all the anchor tags from the page
anchors = soup.find_all('a')
"""print(anchors)"""


# Get 1st paragraph of the HTML page
""" print(soup.find('p')) """


# Get 1st paragraph of the page with its classes
"""print(soup.find('p')['class'])"""


# Get the text from the tags/soup
"""print(soup.find('p').get_text())"""


# Get whole text from the page 
"""print(soup.get_text())"""


# Get all links present in the HTML page
"""
all_links = set()

for link in anchors:
    if(link.get('href') != '#'):
        linktext = "https://codewithharry.com" + link.get('href')
        all_links.add(link)
        print(linktext)
"""

### step 5 : Comments

# Get the comments from the page
"""
markup = "<p><!-- This is a HTML comment --></p>"
soup2 = BeautifulSoup(markup)
# will give you commented stuff
print(type(soup2.p))
# will give a object type
print(type(soup2.p.strings))

"""

