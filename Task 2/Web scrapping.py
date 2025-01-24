                                # WEB SCRAPPER TASK
#-------------------------------------------------------------------------------------------------------------------#


import requests                     
from bs4 import BeautifulSoup       

url = requests.get("https://www.shadowfox.in/")         
print(url.content)                                     

web = BeautifulSoup(url.content,"html.parser")         

print(web.prettify())             

# Displaying Website Title
print(web.title)

# Displaying Website Title Name
print(web.title.name)

# Displaying Website Title String
print(web.title.string)

# Displaying Website Link or Anchor Tag
print(web.a)

# Displaying Website First Para tag
print(web.p)

# Displaying Website First Heading Tag
print(web.h1)

# Finding Website First Anchor tag
print(web.find("a"))

# Finding Website All H1 or Heading Tag
print(web.find_all("h1"))

# Finding Website Data Using id attribute 
print(web.find(id= "nav-bar"))