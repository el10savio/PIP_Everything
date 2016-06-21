# PIP_Everything 
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badge/)    

This is an attempt to develop a python script to download all the PyPi pacakges for python listed in [(pypi index)](https://pypi.python.org/simple/). This is done by parsing the website and then send a os.system command to pip install the package, packages which have already been installed will be upgraded. 

![](https://cdn.meme.am/instances/500x/68841984.jpg)

Dependencies
============

* pip 
* urlib 
* re
* os
* BeautifulSoup 
