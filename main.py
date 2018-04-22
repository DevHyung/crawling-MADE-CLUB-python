import requests
from bs4 import BeautifulSoup
header = {
'Cookie':"__cfduid=d456afab2c873b2d2b9f78c96432e276c1524302950; newsession=ZJdpHDlH%2FO%2BVM8G8IYXjdrB6LNYnWxtKe3QSwJOFpKbSx%2B7V1ld6ubvo471gffiA4aW70ni9lUATYRMTBE88Bw%2BQo6Rb4HqFDea06logQG7DjfCp%2BHYa4mJ0wB%2FGPlcRz9tlQTC1FdifWvrwkW7lCFnXwspTN3poCab8AzmMmIc4zy7QZOnyeuSeNqZP9zngAHkBVRB4V%2F9ajvMMa%2Fxq4URK15HdHp75X68rLxG7CwJeTXfQuZfHyuyaG4PhksvXZwuNdBgiNqTXo78xoOwHAfckSKjh8zc3a9gqzI7tSmrZIbsrQkZarJ4xBP1fKVFXNXBzsDkcUdD6%2B3s6tjzY5lxl7k5mgWatyFFmUSa512Qg%2B8TD3oxkJkDeQAsH1Jm7DQLYeMSgjVY%2BxD7CbZuFAY4P9LAhbNVJ53BN4zZf%2BPI%3D7302345b30bb8b150030c34eceea762ed46b3d16"
}
if __name__=="__main__":
    html = requests.get('http://made-club.com/game/result?type=sport&page=240',headers=header)
    bs4 = BeautifulSoup(html.text,'lxml')
    print( bs4.prettify())