"""Beautiful Soup is a Python library for pulling data out of HTML and XML files.
It works with your favorite parser to provide idiomatic ways of navigating,
searching, and modifying the parse tree. It commonly saves programmers 
hours or days of work."""
from bs4 import BeautifulSoup


import requests #The requests module allows you to send HTTP requests using Python.


URL="https://www.instagram.com/impravin0708" #Profile URL 

#spliting the data 
def parse_data(s):
    #print(s)
    data={}
    s=s.split("-")[0]
    s=s.split(" ")
    data['Followers']=s[0]
    data['Following']=s[2]
    data['Posts']=s[4]
    return data

#Accepting data from instagram 
def scrape_data(username):
    r=requests.get(URL.format(username))
    #print(r)
    s=BeautifulSoup(r.text,"html.parser")
    #print(s)
    meta=s.find("meta",property="og:description")
    return parse_data(meta.attrs['content'])

#Program start 
if __name__ =="__main__":
    username="impravin0708"
    data=scrape_data(username)
    print("Username:",username)
    print("This account has ",data["Followers"]," Followers")
    print("This account has ",data["Following"]," Following")
    print("This account has ",data["Posts"]," Posts")
        
