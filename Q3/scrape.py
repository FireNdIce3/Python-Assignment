from bs4 import BeautifulSoup
import requests


def scrape(id):
  url=f'https://cameochemicals.noaa.gov/chemical/{id}'
  html_text = requests.get(url).text
  soup = BeautifulSoup(html_text,'lxml')
  title = soup.find('h1').text.split()
  if(title[0] == '404'):
    print("Given ID doesn't exist") 
  else:
    name = soup.find('h1',class_="datasheet").text
    cas_number = soup.find('ul',class_="no-bullet3").li.text.split()  
    dict = {"name": name,"cas_number": cas_number[0]}
    return dict
    


