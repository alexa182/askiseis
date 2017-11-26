import requests
from bs4 import BeautifulSoup
from sqlite import read_url,read_title
import random
#self.res = self.soup.findAll('a', {'class': 'img'})
#self.res = items.img['data-src']

#class Scrap:
#
#    lr = read_url()
#
#    def __init__(self, url=lr):
#
#        self.url = url
#        self.r = requests.get(url)
#        self.soup = BeautifulSoup(self.r.content, 'lxml')
#
#        self.article = self.soup.findAll('{}'.format(read_title()))
#        for items in self.article:
#         self.res = items.text
#
#    def __repr__(self):
#        return '{}'.format(self.res)
#
#    def __str__(self):
#        return '{}'.format(self.res)

class Scrap:

    def __init__(self,url="",souptitle=""):

        self.url = url
        self.souptitle = souptitle

    @property
    def url(self):
        li = ['http://aek365.com','http://enwsi.gr']

        for item in li:
            print(item)

        return self.__url

    @url.setter
    def url(self,value):

        if value.isdigit():
            self.__url = value
        else:
            return ("please enter only numbers")

def main():

    print(Scrap())

main()


