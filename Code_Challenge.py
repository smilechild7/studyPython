from tarfile import data_filter
from requests import get
from bs4 import BeautifulSoup

keywords = [
    "flutter",
    "python",
    "javascript"
]

url = "https://remoteok.com/"

def scrape(url, keyword):
    jobs=[]
    Url = f"{url}remote-{keyword}-jobs"
    response = get(Url,
        headers={"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"})
    soup = BeautifulSoup(response.content,"html.parser")
    trs = soup.find_all("tr",class_="job")
    for tr in trs:
        td = tr.find("td",class_="company")
        title = td.find("h2").text
        company = td.find("h3").text
        divs= td.find_all("div",class_="location")
        if (len(divs)==1):
            location = "No data"
            salary = divs[0].text
        else:
            location = divs[0].text
            salary = divs[1].text
        job_data = {
            'title' : title[1:-1],
            'company' : company[1:],
            'location' : location,
            'salary' : salary[:-1]
        }
        jobs.append(job_data)
    return jobs

def make_jobs_dict(url, keywords):
    jobs_dict={}
    for keyword in keywords:
        jobs_dict[f"{keyword}"] = scrape(url, keyword)
    return jobs_dict

dict1 = make_jobs_dict(url, keywords)
print(dict1)