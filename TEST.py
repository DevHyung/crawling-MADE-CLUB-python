from selenium import webdriver
import time
import random
if __name__=="__main__":
    driver = webdriver.Chrome('./chromedriver')
    for qwweqweqweqwe in range(300):
        print(qwweqweqweqwe, "번째 사람중 .. ")
        driver.get(
            'https://docs.google.com/forms/d/e/1FAIpQLSfrP2qAshSjLMPzfdzQhF9FAwZLHGAGIVk8xj9nVQ229uwHTw/viewform')
        time.sleep(2)
        lists = driver.find_elements_by_class_name('freebirdFormviewerViewItemsItemItem')
        answerList = []
        age = ''
        ###1
        tmp = random.randint(0, 100000) % 100
        if tmp <= 10:
            result = 0
        elif tmp <= 40:
            result = 1
        elif tmp <= 75:
            result = 2
        elif tmp <= 95:
            result = 3
        else:
            result = 4
        answerList.append(result)
        age = result
        ###2
        tmp = random.randint(0, 100000) % 100
        if tmp <= 5:
            result = 0
        else:
            result = 1
        answerList.append(result)
        ###3
        if age != 0 or age != 4:
            tmp = random.randint(0, 100000) % 100
            if tmp <= 20:
                result = 0
            elif tmp <= 40:
                result = 1
            elif tmp <= 60:
                result = 2
            elif tmp <= 80:
                result = 3
            elif tmp <= 90:
                result = 4
            else:
                result = 5
        elif age == 0:
            result = 0
        else:
            tmp = random.randint(0, 100000) % 100
            if tmp <= 20:
                result = 1
            elif tmp <= 40:
                result = 2
            elif tmp <= 60:
                result = 3
            elif tmp <= 80:
                result = 4
            else:
                result = 5
        answerList.append(result)
        ###4
        tmp = random.randint(0, 100000) % 100
        if tmp <= 10:
            result = 0
        elif tmp <= 60:
            result = 1
        elif tmp <= 95:
            result = 2
        else:
            result = 3
        answerList.append(result)
        ###5
        tmp = random.randint(0, 100000) % 100
        if tmp <= 10:
            result = 0
        elif tmp <= 60:
            result = 1
        elif tmp <= 80:
            result = 2
        else:
            result = 3
        answerList.append(result)
        ###6
        tmp = random.randint(0, 100000) % 100
        if tmp <= 20:
            result = 0
        else:
            result = 1
        answerList.append(result)
        ###7
        tmp = random.randint(0, 100000) % 100
        if tmp <= 40:
            result = 0
        else:
            result = 1
        answerList.append(result)
        ###7-1
        if result == 0:
            tmp = random.randint(0, 100000) % 100
            if tmp <= 10:
                result = 0
            elif tmp <= 70:
                result = 1
            else:
                result = 2
        else:
            result = -1
        answerList.append(result)
        ###8
        tmp = random.randint(0, 100000) % 100
        if tmp <= 40:
            result = 0
        else:
            result = 1
        answerList.append(result)
        ###9
        tmp = random.randint(0, 100000) % 100
        if tmp <= 10:
            result = 0
        else:
            result = 1
        answerList.append(result)
        ###10
        tmp = random.randint(0, 100000) % 100
        if tmp <= 5:
            result = 0
        elif tmp <= 30:
            result = 1
        elif tmp <= 70:
            result = 2
        else:
            result = 3
        answerList.append(result)
        ###11
        tmp = random.randint(0, 100000) % 100
        if tmp <= 30:
            result = 0
        else:
            result = 1
        answerList.append(result)
        ###11-1
        if result == 0:
            tmp = random.randint(0, 100000) % 100
            if tmp <= 50:
                result = 0
            elif tmp <= 70:
                result = 1
            elif tmp <= 85:
                result = 2
            elif tmp <= 95:
                result = 3
            else:
                result = 4
        else:
            result = -1
        answerList.append(result)
        ###12
        tmp = random.randint(0, 100000) % 100
        if tmp <= 90:
            result = 0
        elif tmp <= 95:
            result = 1
        else:
            result = 2
        answerList.append(result)
        ###12-1
        if result == 1:
            tmp = random.randint(0, 100000) % 100
            if tmp <= 40:
                result = 0
            elif tmp <= 60:
                result = 1
            elif tmp <= 70:
                result = 2
            elif tmp <= 75:
                result = 3
            elif tmp <= 85:
                result = 4
            else:
                result = 5
        else:
            result = -1
        answerList.append(result)
        idx = 0
        for list in lists:
            if answerList[idx] != -1:
                list.find_elements_by_class_name('exportLabelWrapper')[answerList[idx]].click()
                time.sleep(0.1)
            idx += 1
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[3]/div/div/div/content/span').click()
