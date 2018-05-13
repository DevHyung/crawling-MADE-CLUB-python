import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json


class SmartPhone:
    def __init__(self, maker="", model="", spec=[], price=0.0):
        self.Maker = maker
        self.Model = model
        self.Spec = spec[:]
        self.Price = price

    def __str__(self):
        str1 = "--------\n"
        str1 += " Maker: "
        str1 += self.Maker + "\n"
        str1 += " Model: "
        str1 += self.Model + "\n"
        str1 += " Spec: \n"
        for item in self.Spec:
            str1 += "   " + item + "\n"
        str1 += " Price: "
        str1 += str(self.Price) + "\n"
        str1 += "--------\n"

        return str1

    def setInfo(self, maker="", model="", spec=[], price=0.0):
        self.Maker = maker
        self.Model = model
        self.Spec = ""
        self.Price = price

    def addSpec(self, spec):
        self.Spec += spec

header = {
'Cookie': "",
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
}
def GetCookie():
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://made-club.com/login')
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="loginFrm"]/div[1]/input').send_keys(ID)
    driver.find_element_by_xpath('//*[@id="loginFrm"]/div[2]/input').send_keys(PW)
    driver.find_element_by_xpath('//*[@id="btn_login"]').click()
    time.sleep(3)
    tmpstr = '__cfduid=' + driver.get_cookies()[0]['value'] + ';' + 'newsession=' + driver.get_cookies()[1]['value']
    driver.quit()
    return tmpstr
if __name__=="__main__":
    configLines = open('CONFIG.txt').readlines()
    ID = configLines[0].split(':')[1].strip()
    PW = configLines[1].split(':')[1].strip()
    DELAY = int(configLines[2].split(':')[1].strip())
    while True:
        now = time.localtime()
        s = "%02d/%02d" % (now.tm_mon, now.tm_mday)
        saveCookie = open('SESSION.txt').read()
        header['Cookie'] = saveCookie
        html = requests.get('https://made-club.com/sports/cross', headers=header)
        root = {}
        if '<!-- 신규 가입시 환영 메세지 얼럿 --->' in html.text: # 세션끊긴거
            print('>>> Session Re Get .. ')
            cookie = GetCookie()
            f = open('SESSION.txt', 'w')
            f.write(cookie)
            f.close()
            header['Cookie'] = cookie

        #경기결과1
        #print('>>> RESULT1 시작')
        jsonList = []
        jsonList.clear()
        page = '&page='
        pageIdx = 0
        url = 'https://made-club.com/game/result?type=sport'
        LoopGo = True
        while LoopGo:
            if pageIdx == 0:
                html = requests.get(url, headers=header)
            else:
                html = requests.get(url+page+str(pageIdx*30), headers=header)
            pageIdx += 1
            bs4 = BeautifulSoup(html.text, 'lxml')
            table = bs4.find('table', class_='table_1 non_cursor')
            trs = table.find_all('tr')
            for tr in trs:
                data = {}
                try:
                    tc = tr.find('td', class_='tc').get_text().strip()
                    if s == tc[:5]:
                        gameType = tr.find_all('td',class_='tc')[1].get_text().strip()
                        league = tr.find_all('td')[2].get_text().strip()
                        homeTeam = tr.find_all('td')[3].find('td',class_='teamName').get_text().strip()
                        homeRatio = tr.find_all('td')[3].find('td',class_='odd').get_text().strip()
                        drawRatio = tr.find_all('td')[6].get_text().strip()
                        awayTeam = tr.find_all('td')[7].find('td', class_='teamName').get_text().strip()
                        awayRatio = tr.find_all('td')[7].find('td', class_='odd').get_text().strip()
                        homeScore,awayScore = tr.find_all('td')[10].get_text().strip().split(':')
                        gameResult = tr.find_all('td')[11].get_text().strip()
                        data["DateTime"] = tc
                        data["GameType"] = gameType
                        data["League"] = league
                        data["HomeTeam"] = homeTeam
                        data["HomeRatio"] = homeRatio
                        data["DrawRatio"] = drawRatio
                        data["AwayRatio"] = awayRatio
                        data["AwayTeam"] = awayTeam
                        data['HomeScore'] = homeScore.strip()
                        data['AwayScore'] = awayScore.strip()
                        data['GameResult'] = gameResult
                        jsonList.append(data)
                    else:
                        LoopGo = False
                        break
                except:
                    pass
        root['result1'] = jsonList
        # 경기결과2
        #print('>>> RESULT2 시작')
        jsonList = []
        jsonList.clear()
        page = '&page='
        pageIdx = 0
        url = 'https://made-club.com/game/result?type=special'
        LoopGo = True
        while LoopGo:
            if pageIdx == 0:
                html = requests.get(url, headers=header)
            else:
                html = requests.get(url + page + str(pageIdx * 30), headers=header)
            pageIdx += 1
            bs4 = BeautifulSoup(html.text, 'lxml')
            table = bs4.find('table', class_='table_1 non_cursor')
            trs = table.find_all('tr')
            for tr in trs:
                data = {}
                try:
                    tc = tr.find('td', class_='tc').get_text().strip()
                    if s == tc[:5]:
                        gameType = tr.find_all('td', class_='tc')[1].get_text().strip()
                        league = tr.find_all('td')[2].get_text().strip()
                        homeTeam = tr.find_all('td')[3].find('td', class_='teamName').get_text().strip()
                        homeRatio = tr.find_all('td')[3].find('td', class_='odd').get_text().strip()
                        drawRatio = tr.find_all('td')[6].get_text().strip()
                        awayTeam = tr.find_all('td')[7].find('td', class_='teamName').get_text().strip()
                        awayRatio = tr.find_all('td')[7].find('td', class_='odd').get_text().strip()
                        homeScore, awayScore = tr.find_all('td')[10].get_text().strip().split(':')
                        gameResult = tr.find_all('td')[11].get_text().strip()
                        data["DateTime"] = tc
                        data["GameType"] = gameType
                        data["League"] = league
                        data["HomeTeam"] = homeTeam
                        data["HomeRatio"] = homeRatio
                        data["DrawRatio"] = drawRatio
                        data["AwayRatio"] = awayRatio
                        data["AwayTeam"] = awayTeam
                        data['HomeScore'] = homeScore.strip()
                        data['AwayScore'] = awayScore.strip()
                        data['GameResult'] = gameResult
                        jsonList.append(data)
                    else:
                        LoopGo = False
                        break
                except:
                    pass
        root['result2'] = jsonList
        # 경기결과3
        #print('>>> RESULT3 시작')
        jsonList = []
        jsonList.clear()
        page = '&page='
        pageIdx = 0
        url = 'https://made-club.com/game/result?type=live'
        LoopGo = True
        while LoopGo:
            if pageIdx == 0:
                html = requests.get(url, headers=header)
            else:
                html = requests.get(url + page + str(pageIdx * 30), headers=header)
            pageIdx += 1
            bs4 = BeautifulSoup(html.text, 'lxml')
            table = bs4.find('table', class_='table_1 non_cursor')
            trs = table.find_all('tr')
            for tr in trs:
                data = {}
                try:
                    tc = tr.find('td', class_='tc').get_text().strip()
                    if s == tc[:5]:
                        gameType = tr.find_all('td', class_='tc')[1].get_text().strip()
                        league = tr.find_all('td')[2].get_text().strip()
                        homeTeam = tr.find_all('td')[3].find('td', class_='teamName').get_text().strip()
                        homeRatio = tr.find_all('td')[3].find('td', class_='odd').get_text().strip()
                        drawRatio = tr.find_all('td')[6].get_text().strip()
                        awayTeam = tr.find_all('td')[7].find('td', class_='teamName').get_text().strip()
                        awayRatio = tr.find_all('td')[7].find('td', class_='odd').get_text().strip()
                        homeScore, awayScore = tr.find_all('td')[10].get_text().strip().split(':')
                        gameResult = tr.find_all('td')[11].get_text().strip()
                        data["DateTime"] = tc
                        data["GameType"] = gameType
                        data["League"] = league
                        data["HomeTeam"] = homeTeam
                        data["HomeRatio"] = homeRatio
                        data["DrawRatio"] = drawRatio
                        data["AwayRatio"] = awayRatio
                        data["AwayTeam"] = awayTeam
                        data['HomeScore'] = homeScore.strip()
                        data['AwayScore'] = awayScore.strip()
                        data['GameResult'] = gameResult
                        jsonList.append(data)
                    else:
                        LoopGo = False
                        break
                except:
                    pass
        root['result3'] = jsonList
        # 크로스경기
        #print('>>> 크로스 시작')
        jsonList = []
        jsonList.clear()
        html = requests.get('https://made-club.com/sports/cross', headers=header)
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
                dcode = tr.find_all('td')[1]['data-dcode']
                homeTeam = tr.find_all('td')[1]['data-team']
                homeRatio = tr.find_all('td')[1]['data-odds']
                drawRatio = tr.find_all('td')[4]['data-odds']
                awayRatio = tr.find_all('td')[5]['data-odds']
                awayTeam = tr.find_all('td')[5]['data-team']
                data["League"] = league
                data["DateTime"] = tc
                data["HomeTeam"] = homeTeam
                data["HomeRatio"] = homeRatio
                data["DrawRatio"] = drawRatio
                data["AwayRatio"] = awayRatio
                data["AwayTeam"] = awayTeam
                data["data-ts"] = ts
                data["data-league_type"] = leagueType
                data["data-dcode"] = dcode
                jsonList.append(data)
            except:
                pass
        root['cross'] = jsonList

        # 실시간
        #print('>>> 실시간 시작')
        html = requests.get('https://made-club.com/sports/live', headers=header)
        bs4 = BeautifulSoup(html.text, 'lxml')
        table = bs4.find('table', id='gameListTable')
        trs = table.find_all('tr')
        jsonList = []
        jsonList.clear()
        for tr in trs:
            data = {}
            try:
                league = tr.find('th').get_text().strip()
            except:
                pass
            try:
                tc = tr.find('td', class_='tc').get_text()
                ts = tr.find_all('td')[1]['data-ts']
                leagueType = tr.find_all('td')[1]['data-league_type']
                dcode = tr.find_all('td')[1]['data-dcode']
                homeTeam = tr.find_all('td')[1]['data-team']
                homeRatio = tr.find_all('td')[1]['data-odds']
                drawRatio = tr.find_all('td')[4]['data-odds']
                awayRatio = tr.find_all('td')[5]['data-odds']
                awayTeam = tr.find_all('td')[5]['data-team']
                data["League"] = league
                data["DateTime"] = tc
                data["HomeTeam"] = homeTeam
                data["HomeRatio"] = homeRatio
                data["DrawRatio"] = drawRatio
                data["AwayRatio"] = awayRatio
                data["AwayTeam"] = awayTeam
                data["data-ts"] = ts
                data["data-league_type"] = leagueType
                data["data-dcode"] = dcode
                jsonList.append(data)
            except:
                pass
        root['live'] = jsonList
        # 스페셜
        html = requests.get('https://made-club.com/sports/special', headers=header)
        bs4 = BeautifulSoup(html.text, 'lxml')
        table = bs4.find('table', id='gameListTable')
        trs = table.find_all('tr')
        jsonList = []
        jsonList.clear()
        for tr in trs:
            data = {}
            try:
                league = tr.find('th').get_text().strip()
            except:
                pass
            try:
                tc = tr.find('td', class_='tc').get_text()
                ts = tr.find_all('td')[1]['data-ts']
                leagueType = tr.find_all('td')[1]['data-league_type']
                dcode = tr.find_all('td')[1]['data-dcode']
                homeTeam = tr.find_all('td')[1]['data-team']
                homeRatio = tr.find_all('td')[1]['data-odds']
                drawRatio = tr.find_all('td')[4]['data-odds']
                awayRatio = tr.find_all('td')[5]['data-odds']
                awayTeam = tr.find_all('td')[5]['data-team']
                data["League"] = league
                data["DateTime"] = tc
                data["HomeTeam"] = homeTeam
                data["HomeRatio"] = homeRatio
                data["DrawRatio"] = drawRatio
                data["AwayRatio"] = awayRatio
                data["AwayTeam"] = awayTeam
                data["data-ts"] = ts
                data["data-league_type"] = leagueType
                data["data-dcode"] = dcode
                jsonList.append(data)
            except:
                pass
        root['special'] = jsonList
        #f = open('JSON.txt', 'w', encoding='utf8')
        #f.write(json.dumps(root, ensure_ascii=False))
        print(json.dumps(root, ensure_ascii=False))
        time.sleep(DELAY)


