import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
lists = soup.select('#body-content > div > div > table > tbody > tr')

# lists (tr들) 의 반복문을 돌리기
number = 1
for list in lists:
    # list 안에 a 가 있으면,
    a_tag = list.select_one('td.info > a.title.ellipsis')
    if a_tag is not None:
        title = a_tag.text
        artist = list.select_one('a.artist.ellipsis').text
        print(number,title,artist)
        number += 1
