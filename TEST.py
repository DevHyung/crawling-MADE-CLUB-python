from selenium import webdriver
import time
import random
if __name__=="__main__":
    driver = webdriver.Chrome('./chromedriver')
    for qwweqweqweqwe in range(1,100):
        print(qwweqweqweqwe, "번째 사람중 .. ")
        driver.get('https://form.office.naver.com/form/responseView.cmd?formkey=NzUyZTgyYjMtMDA5NC00Zjg4LTg2YjctMmVjMTExZGNkZjk3&sourceId=urlshare')
        time.sleep(random.randint(2,4))

        lists = driver.find_elements_by_class_name('formItemPh')
        answerList = []

        ###1
        tmp = random.randint(0, 100000) % 100
        if tmp <= 90:
            result = 0
        elif tmp <= 98:
            result = 1
        else:
            result = 2

        answerList.append(result)

        ###2
        bandal = 0
        tmp = random.randint(0, 100000) % 100
        if tmp <= 70:
            result = 0
        else:
            result = 1
        bandal = result
        answerList.append(result)
        ###2-1
        result = ''
        if bandal == 0:
            tmp = random.randint(0, 100000) % 100
            if tmp <= 20:
                result = '휴식'
            elif tmp <= 30:
                result = '데이트'
            elif tmp <= 40:
                result = '운동'
            elif tmp <= 45:
                result = '기타'
            elif tmp <= 60:
                result = '지나가는 경로'
            elif tmp <= 80:
                result = '여러목적으로 사용'
            elif tmp <= 90:
                result = '산책'
            else:
                result = '주로 가족들끼리'
        answerList.append(result)
        ###3
        tmp = random.randint(0, 100000) % 100
        if tmp <= 85:
            result = 0
        else:
            result = 1
        answerList.append(result)
        ###4
        tmp = random.randint(0, 100000) % 100
        if tmp <= 60:
            result = 0
        else:
            result = 1
        answerList.append(result)
        ###5
        tmp = random.randint(0, 100000) % 100
        if tmp <= 95:
            result = 0
        else:
            result = 1
        answerList.append(result)

        idx = 0
        for li in lists:
            if idx != 2:
                li.find_elements_by_class_name('radio')[answerList[idx]].click()
            else:
                li.find_element_by_xpath('//*[@id="answer"]').click()
                li.find_element_by_xpath('//*[@id="answer"]').send_keys(answerList[idx])
            time.sleep(0.2)
            idx += 1
        try:
            driver.find_element_by_xpath('//*[@id="pageNav"]/button[3]').click()
        except:
            print("헷")
            pass