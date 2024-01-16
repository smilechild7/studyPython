from requests import get
from bs4 import BeautifulSoup

response =get("https://weworkremotely.com/")

if response.status_code !=200:
    print("Can't access!")
else:
    soup = BeautifulSoup(response.text,"html.parser")
    jobs = soup.find("section",class_="jobs").find_all("li")
    jobs_list=[]
    
    for job in jobs:
        title = job.find("span",class_="title")
        work_form = job.find_all("span", class_="company")
        region = job.find("span",class_="region company")

        job_characteristic = {
            "title" : title,
            "work_form" : work_form[1],
            "region" : region
        }
        jobs_list.append(job_characteristic)

    for job in jobs_list:
        print(job)
        print("//")