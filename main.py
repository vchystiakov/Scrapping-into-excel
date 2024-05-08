# import libraries
import requests
from bs4 import BeautifulSoup
import lxml
from time import sleep

# dictionary with user agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}


# function that downloads item's images in folder
def download(url):
    resp = requests.get(url, stream=True)
    # wb- writes bytes of downloaded image into file
    #!Here must be path to your folder
    r = open('D:\\Courses\\PythonLearning\\Projects\\Scrapping\\Course\\Scrappingintofile\\images\\' +
             url.split("/")[-1], 'wb')
    # 1024x1024(1mb) - is numbers of bytes written by one iteration
    for value in resp.iter_content(1024*1024):
        r.write(value)
    r.close()


# function generator that gets every card item's url
def get_url():
    # using iteration for going through all pages
    for count in range(1, 7):
        # url which will be parsed
        url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'
        # saving request data in variable
        response = requests.get(url=url, headers=headers)
        # parsed object
        soup = BeautifulSoup(response.text, 'lxml')
        # finding every item card block using method find_all
        data = soup.find_all('div', class_="w-full rounded border")
        for i in data:
            # for every item card saves it's url in variable
            card_url = 'https://scrapingclub.com' + i.find("a").get('href')
            # after getting every url function generator stops
            yield card_url


# parser(function) generator that makes request to every url in item card and gets every item info
def array():
    # for every card call function generator
    for card_url in get_url():
        # saving request data in variable
        response = requests.get(card_url, headers=headers)
        # after every request makes pause for 3 seconds
        sleep(1)
        # parsed object
        soup = BeautifulSoup(response.text, 'lxml')
        # for every card url finds its html block
        data = soup.find('div', class_="my-8 w-full rounded border")
        # item name
        name = data.find("h3", class_="card-title").text
        # item price
        price = data.find("h4").text
        # item description
        text = data.find("p", class_='card-description').text
        # item image
        url_image = 'https://scrapingclub.com' + \
            data.find("img", class_='card-img-top').get('src')
        # calling function that will download image of each url
        download(url_image)
        # function stops after getting info of each item and writes it into excel
        yield name, price, text, url_image
