import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.ntv.com.tr/son-dakika#"

    response = requests.get(url)

    içerik = response.content
    soup =  BeautifulSoup(içerik,"html.parser")

    başlıklar = soup.find_all("a",{"class":"card-text-link text-elipsis-3"})

    for i in başlıklar:
        print("*************************************")
        print(i.text)

if __name__ == "__main__":
    main()