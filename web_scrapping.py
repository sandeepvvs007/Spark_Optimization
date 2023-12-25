from bs4 import BeautifulSoup
import re
import requests

# with open("/Users/sandeep/Downloads/homenew.html", 'r') as html_file:
#     content = html_file.read()
    
    # soup = BeautifulSoup(content, 'lxml')
    # s = soup.find_all('p', class_="css-lyyc14 css-w00cnv mt-xsm mb-std")
    # for i in s:
    #     print(i.text)
    
    # # print(soup.prettify())
    # tags = soup.find('h3')
    # tags_all = soup.find_all('h3')
    # # print(tags)
    # # print(tags_all)
    # for headers in tags_all:
    #     pass
    #     # print(headers.text)
    
    # div_cards = soup.find_all('div', class_ = 'row')
    # # print(div_cards)
    # for div in div_cards:
    #     interview_div = div.find_all('div', class_ = 'col-12')
    #     for i in interview_div:
    #         box_div = i.find_all('p', class_="css-lyyc14 css-w00cnv mt-xsm mb-std")
    #         print(box_div)
    #         # for j in box_div:
    #         #     print(j.text)

html_text = requests.get('https://www.cricbuzz.com/live-cricket-scorecard/82717/indw-vs-ausw-only-test-australia-women-tour-of-india-2023-24').text
soup = BeautifulSoup(html_text, 'lxml')
print(soup.find('h2'))
s = soup.find_all('div', class_="cb-col cb-scrcrd-status cb-col-100 cb-text-complete ng-scope")
print(s)
for i in s:
    print(i)