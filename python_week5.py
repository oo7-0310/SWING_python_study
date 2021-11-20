# 게임 매크로 제작
# 1부터 50까지 순서대로 클릭
from selenium import webdriver
import time


driver = webdriver.Chrome()
#driver를 python 설치 경로에 둔 게 아니라면 따로 경로 지정
#path = "C:\Python39\chromedriver.exe"
driver.get("https://zzzscore.com/1to50/")

#driver = webdriver.ChromeOptions()
#driver.add_experimental_option("excludeSwitches", ["enable-logging"])
#browser = webdriver.Chrome(options=driver)
#browser.get("https://zzzscore.com/1to50/")
num=1
while(num<=50):
    btn = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')  # *은 모두를 뜻함, elements -> list 형식으로 가져옴
    for i in btn:
        if i.text == str(num):
            i.click()
            print("클릭"+i.text)
            num+=1
            time.sleep(5)
            

    

