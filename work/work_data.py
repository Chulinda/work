import requests
from bs4 import BeautifulSoup



titles = []
links = []
companies = []
dates = []


def get_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.post(url, headers = headers)
    
    soup = BeautifulSoup(r.text, 'lxml')
    data = soup.find_all('div', class_ = 'card card-hover card-visited wordwrap job-link')

    for i in data:
        title = i.find('h2').text
        titles.append(title)
        # print(title)
        link = 'https://www.work.ua' +i.find('h2').find('a').get('href')
        links.append(link)
        # print(link)
        company = i.find('div', class_ = 'add-top-xs').find('span').find('b').text
        # print(company)
        companies.append(company)
        date = i.find('span', class_ = 'text-muted small').text
        dates.append(date)
        # print(date_)

    return titles, links, companies, dates

# job = input()
# location = input()



def get_pagination_number(location,job):
    base_url = 'https://www.work.ua/ru/jobs-'+location+'-'+job+'/'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


    r = requests.post(base_url, headers = headers)
    soup = BeautifulSoup(r.text, 'lxml')
    pagination = soup.find('ul', class_ = 'pagination hidden-xs')

    if pagination:
        pages = pagination.find_all('li')
        numbers = pages[-2].find('a').text
        numbers = int(numbers)
        if numbers > 1:
            for i in range(1 , numbers+1):
                url = 'https://www.work.ua/ru/jobs-'+location+'-'+job+'/'+'?page='+str(i)
                get_data(url)
            return titles, links, companies, dates

                
        else:
            get_data(base_url)
            return titles, links, companies, dates