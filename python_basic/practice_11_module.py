# import theater_module
# theater_module.price(3) # 3명이서 영화 보러 갔을 떄
# theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때 
# theater_module.price_soldier(5) # # 군인 아조씨 5명

# import theater_module as mv # theater_module이라는 말이 너무 기니 약자로 바꿔 정의 할 수 도 있다.
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import * # from random import *과 같은 원리 
# # 이건 약어까지 생략 가능
# price(3)
# price_morning(4)
# price_soldier(5)


'''from theater_module import price, price_morning
price(5)
price_morning(6)
# 내가 제대한 민간인 이라는 가정하에 모듈을 선언함, 이 경우 price_soldier 함수를 호출 하면 오류가 뜸 

from theater_module import price_soldier as price
price(5) # price_soldier를 price라는 약아로 쓸거야 라고 명시하고 쓰는 것
'''


# 패키지
# import travel.thailand # 맨 뒤에 있는 부분은 항상 모듈이나 패키지만 가능하다 . 클래스나 함수 import->x
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()
# from import 로는 사용가능함

# from travel.thailand import ThailandPackage
# trip_to=ThailandPackage()
# trip_to.detail()

# from travel.vietnam import VietnamPackage
# trip_to=VietnamPackage()
# trip_to.detail()


# from random import *
'''from travel import *
# trip_to = vietnam.VietnamPackage() # 공개 범위를 설정하지 않을시 import *를 해도 이 파일을 불러오지 못한다
# trip_to.detail()
# trip_to=thailand.ThailandPackage()
# trip_to.detail()

# python 모듈위치
# 지금까지의 패키지와 모듈은 pratice.py의 위치와 동일한 위치에 있거나
# 파이썬내의 라이브러리 내에 있어야지만 호출이 가능했다. / 그 파일의 위치를 알아내는 클래스함수=inspect 
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))
'''
#pypi를 통해서 패키지를 다운 받을 수 있다.
# 웹스크레핑으로 유명한 뷰티풀수프를 다운받아본다.

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# 내장 함수 : 따로 import 할 필요 없이 사용할 수 있는 함수
# language = input("무슨 언어를 좋아해? : ")
# print('{}언어는 아주 좋은 언어야'.format(language))

# dir : 어떤 객체를 넘겨줬을 떄 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random 
# # print(dir())
# # import pickle
# # print(dir())

# print(dir(random)) # random +. 했을떄 나오는 명령어들, 즉 사용할 수 있는 명령어를 출력해준다.

# lst = [1,2,3]
# print(dir(lst))

# name = 'jimin'
# print(dir(name))
# # list of python builtins  

## 외장함수 -> import 해야 하는 함수들
# list of python index

# glob : 경로내의 폴더/  파일 목록 조회(윈도우 DIR)
# import glob
# print(glob.glob('*.py')) # 확장자가 PY인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
import os 
# print(os.getcwd)# 현재 디렉터리 표시

# forder = 'sample_dir'
# if os.path.exists(forder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(forder)
#     print(forder,'폴더를 삭제하였습니다.')
# else:
#     os.makedirs(forder)#폴더생성
#     print(forder,"폴더를 생성합니다. ")
# print(os.listdir()) # glob 함수와 비슷한 역할을 한다.

# import time 
# print(time.localtime()) # 분초 단위로 시간을 세밀하게 표시해줌
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
# print('오늘날짜는', datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은",today+td)