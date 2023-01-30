from random import *

# print(random()) # 0.0~1.0  미만의 임의의 값 생성
# print(random()*10)#0.0~10.0 미만의 임의의 값 생성
# print(int(random()*10))

# print(int(random()*45)+1)
# print(randrange(1,46))
# print(randint(1,45))

date = randint(4,28)
print('오프라인 스터디 모임 날짜는 매월, {0} 일로 선정되었습니다.'.format(date))