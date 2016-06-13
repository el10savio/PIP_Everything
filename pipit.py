import urllib
import re
import os
from bs4 import BeautifulSoup

def getWords(text):
    return re.compile('\w+').findall(text)
def words(text): return re.findall('[a-z]+', text.lower()) 

url = "https://pypi.python.org/simple/"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)
print('*****************************************************')

#TODO: 1.Split text words into a list.
#      2.Run os.system pip command (along with --upgrade)

packages = getWords(text)
for i in packages:
           	  print("INSTALLING:"+i)
		  command ="sudo pip install --upgrade "+i
		  os.system(command)
    

