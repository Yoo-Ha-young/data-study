import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def getDays(year, month):
    # 1일
    first_day = datetime(year, month, 1)

    # 마지막 날
    if month == 12:
        last_day = datetime(year + 1, 1, 1) - timedelta(days=1)
    else:
        last_day = datetime(year, month + 1, 1) - timedelta(days=1)

    # 모든 날짜 구하기
    current_day = first_day
    dates_in_month = []
    while current_day <= last_day:
        dates_in_month.append(current_day.strftime("%Y%m%d"))
        current_day += timedelta(days=1)

    # 결과 출력
    return dates_in_month

def getData(url):
    web = requests.get(url)
    return BeautifulSoup(web.text, "html.parser")


def getDataWithHeader(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
    web = requests.get(url, headers=headers)
    return BeautifulSoup(web.text, "html.parser")

def getPageUrl(url, page):
    pageUrl = url + str(page)
    return pageUrl

# CSV 파일에 데이터를 추가하는 메서드
def appendDataToCsv(file_name, data):
    with open(file_name, 'a', newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

