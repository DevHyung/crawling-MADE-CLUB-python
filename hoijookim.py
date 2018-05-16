"""
title           :
description     : 나이입력 받아 최고령,최연소, 평균연령,연령대분포 뽑아냄
author          :
date            : 2018.05.16
version         : 1.0.0
usage           : python3 main.py
python_version  : 3.6
required module :
"""
def menu():
    """

    :return: 입력된 메뉴 번호
    """
    print('-' * 50)
    print("입력된 연령", ageList)
    print('=' * 50)
    print('1. 최고령')
    print('2. 최연소')
    print('3. 평균연령')
    print('4. 연령대의 분포')
    print('5. 종료')
    print('-'*50)
    return int(input()) #선택번호 리턴
def getHighAge(ageList):
    """
    :param ageList: 나이저장된 배열
    :return: 최고령이 포함된 String 문구 print
    """
    maxAge = -1 #입력받을수있는 범위보다 작은값을 먼저 선정
    for age in ageList: # agelist 순회후
        if maxAge < age: # age가 더크면
            maxAge = age #값변경
    print('<최고령은 {}세 입니다.>'.format(maxAge))
def getLowAge(ageList):
    """

    :param ageList: 나이저장된 배열
    :return: 최연소 나이가 포함된 String 문구 print
    """
    minAge = 111 # 입력받을수있는 범위보다 큰값을 먼저 선정
    for age in ageList:  # agelist 순회후
        if minAge > age:  # min값이 더크면
            minAge = age  # 값변경
    print('<최연소는 {}세 입니다.>'.format(minAge))
def averageAge(ageList):
    """

    :param ageList: 나이저장된 배열
    :return: 나이의 평균연령 포함된 String 문구 print
    """
    aver = 0
    for age in ageList:  # agelist 순회후
        aver += age #전체값을 계속더한후
    aver = aver / len(ageList) #배열의 갯수로 나눠줌
    print('<평균연령은 {}세 입니다.>'.format(aver))

def distributionAge(ageList):
    """
    :param ageList: 나이저장된 배열
    :return: 연령대 분포가 포함된 String 문구 Print
    """
    # 봐야하는건
    # 10대미만, 10대, 20대, 30대 , 40대, 50대이상으로
    # 나이를 10으로 나눈 몫을 가지고 연령대 구분을 판별하는 알고리즘을 사용

    distList = [0,0,0,0,0,0] # 10대미만, 10대 .... 등 몇명인지를 차례대로 0으로 초기화한 배열 생성
    for age in ageList:  # agelist 순회
        quot = age // 10 # 앞자리수 판별 10으로 나눈 몫을 본다
        if quot > 5: # 50대 이상이면
            distList[5] += 1
        else:
            distList[quot] += 1
    # 앞에 출력될 문구를 리스트로 저장해서 편하게 출력
    printStrList = ['10대미만','10대','20대','30대','40대','50대이상']
    for idx in range(len(printStrList)):
        print('[{}] - {} 명'.format(printStrList[idx],distList[idx]))

if __name__=="__main__":
    ageList = [] # 입력된 나이를 저장하는 배열
    # 나이 입력부분
    print('5명의 나이를 입력하세요.')
    for idx in range(5): # 5명의 나이를 입력받아야하니 5번 반복
        while True: # 제대로된 나이가 입력될때까지
            age = int ( input('[{}번째 연령]? '.format(idx+1)) )
            if age < 0 or age > 110: # 제대로 입력이 안될시에
                print('나이는 0~110세 까지 가능 합니다. 다시 입력해 주세요.')
            else: # 제대로 입력됨
                ageList.append(age) #나이저장후
                break # 반복문 탈출
    # 나이 입력 끝
    while True: #계속해서 입력받으면서 계산작업을 하는 루프
        selectNum = menu()
        if selectNum == 1: # 최고령
            getHighAge(ageList)
        elif selectNum==2:
            getLowAge(ageList)
        elif selectNum == 3:
            averageAge(ageList)
        elif selectNum ==4:
            distributionAge(ageList)
        elif selectNum == 5:
            break




