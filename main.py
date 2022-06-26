import requests
import logging as log



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
 
    def __init__(self, responseFormat="json", proxies=None, verbose=False):
        self.responseFormat=responseFormat
        self.__url=None
        self.proxies=proxies
        self.searchType=None
        self.verbose=verbose
        # Automatically determine searchtype
        # if not phoneNumber:
        #     self.set_url("phonebook_search")
        # elif phoneNumber.isnumeric():
        #     self.set_url("number_search")
        # else:
        #     raise TypeError("Check phone number")




obj=web_api(verbose=True)
print(obj.search_phone(6920234234))

    
