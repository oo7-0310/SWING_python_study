import os #os모듈, 운영체제에서 제공되는 여러 기능을 파이썬에서 수행할 수 있게 한다
import urllib.request #URL을 열기 위한 확장 가능한 라이브러리
from bs4 import BeautifulSoup 

opener=urllib.request.build_opener() 
opener.addheaders=[( 'User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')] 
urllib.request.install_opener(opener) 




web = urllib.request.urlopen('https://comic.naver.com/webtoon/list?titleId=524520&weekday=fri') # 첫 페이지(가장 최근회차 포함 10화)
soup = BeautifulSoup(web, 'html.parser')

trump = soup.find("div",{"class": "detail"}).select_one('span').parent.text.strip().split() # 웹툰제목과 작가이름이 같이 나와서 split로 나눠주고 인덱스 0에 있는 웹툰 이름만 사용함/strip()은 줄바꿈없애기/h2를 기준으로 하니까 웹툰제목, 작가이름 둘다 나와서 span에 parent를 하면 웹툰제목만 얻을 수 있지 않을까 했는데 똑같았음

os.mkdir(trump[0]) #웹툰이름으로 폴더 생성
os.chdir(trump[0]) #웹툰 폴더를 작업 디렉토리로 변경

for title in soup.find_all("td",{"class": "title"}): #클래스명이 title인 <td> 태그 모두 찾기
   os.mkdir(title.text.strip()) # 해당 태크의 text 부분(회차정보)만 가져오는데 앞뒤에 줄바꿈 붙어있으므로 strip()써서 없앤 후 디렉토리 생성 ex.시즌4 85화 궤도 9
   os.chdir(title.text.strip()) # 만든 디렉토리로 작업 디렉토리로 변경

   url = "https://comic.naver.com"+title.find("a")["href"] #웹툰 회차 클릭 시 이동하는 url
   web2 = urllib.request.urlopen(url) #url 가져오기 위한 함수 모듈
   soup2 = BeautifulSoup(web2, 'html.parser')
   num = 1 #이미지 저장할 때 파일명으로 사용
   
   tmp = soup2.find("div",{"class": "wt_viewer"}) # div 태그의 wt_viewer 클래스 내용을 가져오는데
   for img in tmp.findAll('img'): #그 중 img 태그를 다 긁어오고
       urllib.request.urlretrieve(img['src'],str(num)+".jpg") #urlretrieve(이미지경로, 저장경로+저장파일명) 형식임. img태그에서 src 값이 이미지주소로 쓰이고, 저장경로는 현재 위치에 저장할 거기 때문에 생략하면 됨, 숫자.jpg로 저장
       num+=1

   os.chdir("..") #이전 폴더인 '트럼프'로 이동









