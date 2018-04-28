import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json

header = {
'Cookie': "",
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
}
def GetCookie():
    driver = webdriver.Chrome('./chromedriver')
    driver.get('http://made-club.com/login')
    driver.find_element_by_xpath('//*[@id="loginFrm"]/div[1]/input').send_keys('Vie111')
    driver.find_element_by_xpath('//*[@id="loginFrm"]/div[2]/input').send_keys('1234')
    driver.find_element_by_xpath('//*[@id="btn_login"]').click()
    time.sleep(3)
    str = '__cfduid=' + driver.get_cookies()[0]['value'] + ';' + 'newsession=' + driver.get_cookies()[1]['value']
    #driver.quit()
    return str
if __name__=="__main__":
    saveCookie = open('SESSION.txt').read()
    header['Cookie'] = saveCookie
    html = requests.get('http://made-club.com/game/result?type=sport&page=240', headers=header)
    jsonList = []
    if '<!-- 신규 가입시 환영 메세지 얼럿 --->' in html.text: # 세션끊긴거
        print('>>> Session Re Get .. ')
        cookie = GetCookie()
        f = open('SESSION.txt', 'w')
        f.write(cookie)
        header['Cookie'] = cookie
    # 크로스경기
    html = requests.get('http://made-club.com/sports/cross', headers=header)
    bs4 = BeautifulSoup(html.text, 'lxml')
    table = bs4.find('table',id='gameListTable')
    trs = table.find_all('tr')
    for tr in trs:
        data = {}
        try:
            league = tr.find('th').get_text().strip()
        except:
            pass
        try:
            tc = tr.find('td',class_='tc').get_text()
            ts = tr.find_all('td')[1]['data-ts']
            leagueType = tr.find_all('td')[1]['data-league_type']
            homeTeam = tr.find_all('td')[1]['data-team']
            homeRatio = tr.find_all('td')[1]['data-odds']
            drawRatio = tr.find_all('td')[4]['data-odds']
            awayRatio = tr.find_all('td')[5]['data-odds']
            awayTeam = tr.find_all('td')[5]['data-team']
            data["League"] = league
            data["DateTime"] = tc
            data["LeagueType"] = leagueType
            data["HomeTeam"] = homeTeam
            data["HomeRatio"] = homeRatio
            data["DrawRatio"] = drawRatio
            data["AwayRatio"] = awayRatio
            data["data-ts"] = ts
            jsonList.append(data)
        except:
            pass
    f = open('JSON.txt','w',encoding='utf8')
    f.write(json.dumps(jsonList, ensure_ascii=False))
    print(json.dumps(jsonList, ensure_ascii=False))

