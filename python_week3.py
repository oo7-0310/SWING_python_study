import urllib.request
from bs4 import BeautifulSoup #텍스트 형태의 데이터에서 원하는 html 요소에 접근하는 데 필요, html을 객체로 만들어 사용자가 쓰기 쉽게 만듦

#beautifulSoup 객체 생성
web = urllib.request.urlopen('http://www.swu.ac.kr/www/swuniversity.html')

soup = BeautifulSoup(web, 'html.parser')


print("*** 서울여자대학교 학과 및 홈페이지 정보 ***\n\n")
print("학과                              홈페이지\n")


for href in soup.find_all("li"):
    url = "http://www.swu.ac.kr"+href.find("a")["href"]
    web2 = urllib.request.urlopen(url)
    soup2 = BeautifulSoup(web2, 'html.parser')
    tmp = soup2.select('div.section')
    url2 = tmp[3].find("a")["href"]
    if( url2[0] != 'h'):
        url2 = "홈페이지가 존재하지 않음"
    print(href.text, "                    ", url2)
  