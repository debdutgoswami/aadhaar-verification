from bs4 import BeautifulSoup

def check_exist(response):
    soup = BeautifulSoup(response, 'html.parser')
    tags = soup('h2')
    if(len(tags)>1):
        status = tags[1].decode()[18:53]
        print(status)
    else:
        print("Invalid CAPTCHA or network error!")