from os import error
import urllib.request
from bs4 import BeautifulSoup #텍스트 형태의 데이터에서 원하는 html 요소에 접근하는 데 필요, html을 객체로 만들어 사용자가 쓰기 쉽게 만듦

#beautifulSoup 객체 생성
web = urllib.request.urlopen('http://www.swu.ac.kr/www/swuniversity.html') # 첫 페이지

soup = BeautifulSoup(web, 'html.parser')


print("*** 서울여자대학교 학과 및 홈페이지 정보 ***\n\n")
print("학과                              홈페이지\n")


for href in soup.find_all("li"): #url이 모두 각각의 li 태그 안에 있어서 기준으로 삼음
    url = "http://www.swu.ac.kr"+href.find("a")["href"] # 첫베이지 코드에서 얻은 사이트 주소(href)를 가져와서 다음 페이지로 넘어가도록 저장, http://www.swu.ac.kr은 공통
    web2 = urllib.request.urlopen(url)
    soup2 = BeautifulSoup(web2, 'html.parser')
    try:
        url2 = soup2.find("a", {"class":"btn btn_xl btn_blue_gray"})['href'] # 학과 홈페이지가 해당 클래스의 href값에 있기 때문에 이 부분을 출력해주는데
    except:
        url2 = "홈페이지가 존재하지 않음" #오류(ex.공공기기실)가 날 경우 그냥 넘어가도록 예외처리 해주고 "홈페이지가 존재하지 않음"출력하도록 해줌
 
    if( url2[0] != 'h') :#오류는 안나지만 다른 링크를 저장하고 있어도 홈페이지 없다고 출력
        url2 = "홈페이지가 존재하지 않음"
    print(href.text, "                    ", url2) 
  
  
