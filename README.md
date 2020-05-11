# Amazon-Scrape and Ebay-Scrape
(Ebay portion in progress)
A web scrapper that scrapes search results on Amazon or Ebay. Gets the name, price, rating, product link, and image link of each listing and exports it to a csv file. Uses rotating proxies and user agents so there is less chance of being detected by Amazon. You can disable the rotating proxies by commenting out these two lines of code in settings.py

```
'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. When creating your own virtual environment make sure to delete the Lib and Scripts folders from this repository.

### Prerequisites

You will need python 3 and pip installed. Pip usually comes with python 3 but if it is not use this command to install pip:

```
python get-pip.py
```
Also, install virtualvenv with the command:
```
pip install virtualenv
```

### Installing

A step by step series of examples that tell you how to get a development env running

1. Create a virtual environment in the directory in which you plan to keep the project. Run this command to create the virtual environment:
```
virtualenv env
```
  To activate the virtual environment run this command if using windows:
```
./Scripts/activate
```
  If using linux use:
```
./bin/activate
```
2. Install scrapy with the command:
```
pip install scrapy
```
3. Install rotating proxies for scrapy with the command:
```
pip install scrapy-rotating-proxies
```
4. Install selenium with the command:
```
pip install selenium
```
   Install chromedriver from https://chromedriver.chromium.org/downloads and set the chromedriver variable in GetUrl.py to the exact path that it is saved to on your computer.
   
5. Install bs4 with the command:
```
pip install bs4
```
6 Install pandas with the command:
```
pip install pandas
```
7. Now start a scrapy project with the command:
```
scrapy startproject project_name
```
   Then cd into the "project_name" directory
   
8. Create a spider with the command:
```
scrapy genspider example
```
9. Now run the project with the command:
```
scrapy crawl example
```
   Then just type into the console/terminal what you want the csv file to be called and then what you want to search on Amazon.
   

## Built With

* (https://docs.scrapy.org/en/latest/) - The web scrapping framework used
* (https://github.com/TeamHG-Memex/scrapy-rotating-proxies) - The scrapy rotating proxies framework used
* (https://www.selenium.dev/) - Framework used in addition to scrapy
* (https://pandas.pydata.org/) - Csv modification framework used
* (https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Framework used to scrape github repository of proxies
* (https://github.com/clarketm/proxy-list) - The proxy list used to rotate proxies

