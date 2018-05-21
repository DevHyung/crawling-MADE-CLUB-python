tmp = input()
sum = 0
isStart = False
numstr = ''
for ch in tmp:
    if ch.isdigit():
        if not isStart: # False일때
            numstr +=  ch
            isStart = True
        elif isStart: # True 일떄
            numstr += ch
            isStart = False #두글짜니까
        if len(numstr) == 2:

            sum += int(numstr)
            numstr = ''
print(sum)

exit(-1)
import requests
from bs4 import BeautifulSoup
import time
import json
##
header = {
'Cookie': '',
'Upgrade-Insecure-Requests':'1',
'Accept-Encoding':'gzip, deflate',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
'Accept-Language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
}
def GetCookie():
    millis = int(round(time.time() * 1000))
    url = 'https://made-club.com/login/auth?type=login&oper=login&nd=' + str(millis)
    formdata = {
        'id': 'a312d2dc1b6b00e575ad93735a21dd5689c54cec2a179c61b22520aafece564a531890f9b5d943b0786f1ed8645708a125b03a889894917e070fa935ec3664997a4f3ca50f6d280b43e847c371251dc893fa58f059041897b1811cbb4ed94528fb4d3b74480854a912745619a66c1e3b2cf8fbab00628d38725c978394e21778',
        'password': 'ad9a6621a1e86ba6dd4a97c60c24bee67f1cb2577fe9223ac5a8180e0880f9959545e1b627eed5b64d2b4115ead6e2e8c5cc4eca43eb0f457f439acbaa55aa998cb325ace4b4ceb2222d26d853b6275326b4ea959fe723b004e0f027d2f14cb287dcb4b28693d0fe4a30f1d38e005104e5f310b7df5eea9384352e1bb5dc9702'
    }
    res = requests.post(url, data=formdata)
    tmpstr = '__cfduid=' + res.cookies.get('__cfduid').strip() + ';' + 'newsession=' + res.cookies.get(
        'newsession').strip()
    return tmpstr
if __name__=="__main__":
    configLines = open('CONFIG.txt').readlines()
    ID = configLines[0].split(':')[1].strip()
    PW = configLines[1].split(':')[1].strip()
    DELAY = int(configLines[2].split(':')[1].strip())
    now = time.localtime()
    s = "%02d/%02d" % (now.tm_mon, now.tm_mday)
    saveCookie = open('SESSION.txt',encoding='utf8').read().strip()
    header['Cookie'] = saveCookie
    html = requests.get('https://made-club.com/sports/cross', headers=header)
    root = {}

    if '<!-- 신규 가입시 환영 메세지 얼럿 --->' in html.text: # 세션끊긴거
        print('>>> Session Re Get .. ')
        cookie = GetCookie()
        f = open('SESSION.txt', 'w',encoding='utf8')
        f.write(cookie.strip())
        f.close()
        header['Cookie'] = cookie.strip()
    try:
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
        print(json.dumps(root, ensure_ascii=False))
    except:
        exit(1)
    exit(0)