import urllib.request
from bs4 import BeautifulSoup #텍스트 형태의 데이터에서 원하는 html 요소에 접근하는 데 필요, html을 객체로 만들어 사용자가 쓰기 쉽게 만듦

#beautifulSoup 객체 생성
web = urllib.request.urlopen('http://www.swu.ac.kr/www/swuniversity.html') # 첫 페이지

soup = BeautifulSoup(web, 'html.parser')


print("*** 서울여자대학교 학과 및 홈페이지 정보 ***\n\n")
print("학과                              홈페이지\n")


for href in soup.find_all("li"):
    url = "http://www.swu.ac.kr"+href.find("a")["href"] # 첫베이지 코드에서 얻은 사이트 주소(href)를 가져와서 다음 페이지로 넘어가도록 저장, http://www.swu.ac.kr은 공통
    web2 = urllib.request.urlopen(url)
    soup2 = BeautifulSoup(web2, 'html.parser')
    tmp = soup2.select('div.section') # 새로 사이트를 soup2로 설정해줬고, div 태크의 section 클래스를 tmp로 가져온 후
    url2 = tmp[3].find("a")["href"] # 의도하신 게 아닌것 같음(1)코드를 보면 section 클래스가 여러 개 있는데 홈페이지는 3 인덱스에 위치함, a 태그 안의 href인 주소를 가져와서 출력
    if( url2[0] != 'h'):#이걸 의도하신 게 아닐텐데(2) 어차피 홈페이지는 h로 시작하기 때문에 아닐 때를 홈페이지가 없다고 출력하게끔 설정
        url2 = "홈페이지가 존재하지 않음"
    print(href.text, "                    ", url2) #근데 수학과까지만 되고 그 이후에 오류 나서 인덱스로 접근이 아닌 것 같음
  