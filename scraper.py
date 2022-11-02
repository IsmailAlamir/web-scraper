import requests
from bs4 import BeautifulSoup

def get_Data(url):
    """
    this function take the url and get all page content from this url 
    then extract all paragraph that need citations 
    and return it as list
    """
    page=requests.get(url)
    content=BeautifulSoup(page.content,"html.parser")
    all=content.find_all("sup",class_="noprint Inline-Template Template-Fact")
    return all


def get_citations_needed_count(url):
    """
    this function take the url and run the get_Data function 
    then print the count of all paragraph that need citations
    """
    print(len(get_Data(url)))


def get_citations_needed_report(url):
    """
    this function take the url and run the get_Data function 
    then print paragraphs that need citations    
    """
    for paragraph in get_Data(url) :
        print(paragraph.parent.text)



get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico")
get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico")