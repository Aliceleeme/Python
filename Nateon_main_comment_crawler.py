
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

#https://beomi.github.io/2017/02/27/HowToMakeWebCrawler-With-Selenium/

def recommend(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    recommend_list = soup.select('.btnwrap .count')
    print("댓글수 :", soup.select('.cmt_tit .num')[0].text)
    print("추천 :", recommend_list[0].text)
    print("반대 :", recommend_list[1].text)


#Search keyword
keyword = input("검색어를 입력하십시오: ")
binary= '/Users/jihye/Documents/chromedriver_mac64/chromedriver'
driver = webdriver.Chrome(binary)
driver.get('http://pann.nate.com/search/talk?q='+keyword)
driver.find_element_by_xpath("""//*[@id="GnbWrap"]/div[2]/a""").click()
driver.find_element_by_name("ID").send_keys("nateon_id")       #접속하려는 페이지 아이디
driver.find_element_by_name("PASSWD").send_keys("nateon_passcode")          #접속하려는 페이지 패스워드
driver.find_element_by_xpath('//*[@id="tab_cont1"]/div/input').click()
 
for i in range(1,3):
    print("Page"+str(i))
    print("\n")
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    subject_list = soup.select('.subject')
    driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/div[4]/a['+str(i)+']').click()
    for idx, subject in enumerate(subject_list, 1):
        print(idx, subject.text.strip(),subject['href'])
        recommend(subject['href'])
    print("\n")

    #selenium을 통한 네이트판 게시물 타이틀과 댓글 가져오기 
#원본코드: http://blog.naver.com/nike_review/221050227966

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

binary= '/Users/jihye/Documents/chromedriver_mac64/chromedriver'
driver=webdriver.Chrome(binary)

driver.get('http://pann.nate.com/talk/c20011')
driver.find_element_by_xpath("""//*[@id="GnbWrap"]/div[2]/a""").click()
driver.find_element_by_name("ID").send_keys("id")       #접속하려는 페이지 아이디
driver.find_element_by_name("PASSWD").send_keys("pw")          #접속하려는 페이지 패스워드
driver.find_element_by_xpath("""//*[@id="tab_cont1"]/div/input""").click()

def search_pann(url):
        html = requests.get(url).text
        soup = BeautifulSoup(html,'html.parser')
        reply_list = soup.select('.usertxt')
        if len(reply_list) == 0:
            print("댓글이 없습니다")
        else:
            try:
                print("베스트 1위 댓글 :", reply_list[0].text.strip())
                print("베스트 2위 댓글 :", reply_list[1].text.strip())
                print("베스트 3위 댓글 :", reply_list[2].text.strip())
            except:
                pass

for i in range(1,11):
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    tag_list = soup.select('.subject > a')
    #driver.find_element_by_xpath('//*[@id="searchDiv"]/div[1]/div/a['+str(i)+']').click()
    driver.find_element_by_xpath("//div[@id='searchDiv']/div[@class='posting_wrap']")   
    #참고코드: https://wkdtjsgur100.github.io/selenium-xpath/
    for idx, a_tag in enumerate(tag_list,1):
        print("\n")
        print(idx, a_tag.text.strip())
        search_pann(a_tag['href'])
    import requests
