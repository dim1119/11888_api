from tabnanny import verbose
import requests
import logging as log
from bs4 import BeautifulSoup
import json 


class web_api:

    def set_url(self,searchType):
        if searchType=="number_search":
            self.__url="https://www.11888.gr/antistrofh-anazhthsh-me-arithmo-thlefwnou/?phone="
        elif searchType=="phonebook_search":
            self.__url="https://www.11888.gr/white-pages/"
        else:
            raise TypeError("Invalid option")



    def search_phone(self,phoneNumber):
        if not phoneNumber or not isinstance(phoneNumber, int):
            raise TypeError("Check phone number")

        self.__url="https://www.11888.gr/antistrofh-anazhthsh-me-arithmo-thlefwnou/?phone="
        query=self.__url+ str(phoneNumber)

        if self.verbose:
            log.info("Quering: " + query)

        # Header to receive JSON and agent
        headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36'
            }

        responseJSON = requests.get(query,headers=headers).json()
        
        # Sanity Check
        if not responseJSON['status']=="ok":
            log.error("Status:" + responseJSON['status'] + " " + "Code:" + str(responseJSON['code']))


        # Keep data only
        responseJSON=responseJSON["data"]["results"]

        if verbose==True:
            log.info("Searched for " + responseJSON["number"])

        # for key in responseJSON["wp"].keys():
        #     print(key)
        try:
            Results = responseJSON["wp"][0]
        except:
            print(responseJSON["wp"])
        print(Results["name"])




    def __init__(self, responseFormat="json", proxies=None, verbose=False):
        self.responseFormat=responseFormat
        self.__url=None
        self.proxies=proxies
        self.searchType=None
        self.verbose=verbose



        if verbose:
            log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
            log.info("Verbose output.")
        else:
            log.basicConfig(format="%(levelname)s: %(message)s")
        # Automatically determine searchtype
        # if not phoneNumber:
        #     self.set_url("phonebook_search")
        # elif phoneNumber.isnumeric():
        #     self.set_url("number_search")
        # else:
        #     raise TypeError("Check phone number")




obj=web_api(verbose=True)
#obj.search_phone(6936721271)
obj.search_phone(6969696969)

