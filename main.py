import csv
from playwright.sync_api import sync_playwright
import time 
from bs4 import BeautifulSoup
p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
page = browser.new_page()

page.goto("https://www.wanted.co.kr/search?query=flutter&tab=position")
# time.sleep(1)

# page.click("button.Aside_searchButton__Xhqq3")
# time.sleep(1)

# page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")
# time.sleep(1)

# page.keyboard.down("Enter")
# time.sleep(2)

# page.click("a#search_tab_position")
# time.sleep(4)

for i in range(5):
    page.keyboard.down("End")  
    time.sleep(2)

content = page.content()
p.stop()

soup = BeautifulSoup(content,"html.parser")
divs = soup.find_all("div",class_="JobCard_container__FqChn")

jobs = []
for div in divs:
    
    link = f"https://www.wanted.co.kr{div.find('a')['href']}"

    title = div.find("strong",class_="JobCard_title__ddkwM").text
    company = div.find("span",class_="JobCard_companyName__vZMqJ").text
    location = div.find("span",class_="JobCard_location__2EOr5").text
    reward = div.find("span",class_="JobCard_reward__sdyHn").text
    
    job_data = {
    
        "title" : title,
        "company" : company,
        "location" : location,
        "reward" : reward,
        "link" : link,
    }

    jobs.append(job_data)

file = open("jobs.csv", "w") # 존재하지 않으면 새로 만듬, w는 쓰기 모드 (기본은 "r" 읽기)
writer = csv.writer(file)
writer.writerow(["Title","Comapany","Location","Reward","Link"]) #writerow 메서드는 list를 받는다
for job in jobs:
    writer.writerow(job.values())
file.close()