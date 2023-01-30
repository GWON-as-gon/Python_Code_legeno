from random import *

# print('{0: <10}'.format(500))
# print('{0: >+10}'.format(500))
# print('{0: <+10}'.format(-500))
# print('{0:,}'.format(10000000000))

# print('{0:ㅎ<+30,}'.format(10000000000)) #빈공간을 뭐로 채울지가 가장 우선시된다. 그 다음은 정렬, 플마 기호, 공간 얼마나 확보 할지, 콤마 순

# # lotto_gomi 
# lotto=[] 
# for i in range(6):
#     i=randint(1,46) # 순서1
#     while i in lotto: #3
#         i=randint(1,46)#4
#     lotto.append(i)  #2
# print(lotto)#5 

'''
class Unit:
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp

class flyable:
    def __init__(self,location):
        self.location=location
        print('{0}시 방향으로 날아가는 중'.format(self.location))


class Attack_unit(Unit):
    def __init__(self, name,hp,damage):
        self.damage=damage
        Unit.__init__(self, name, hp)
    def attack(self,location):
        print("{0}:{1} 방향으로 적군을 공격 합니다, [공격력 {2}".format(self.name, location, self.damage))
    def damaged(self, damaged):
        print('{0}이 {1}의 데미지를 받았습니다.'.format(self.name,damaged))
        self.hp-=damaged
        print('현재 체력 {}'.format(self.hp))     
        if self.hp<=self.damage:
            print('{0} 유닛이 파괴되었습니다.'.format(self.name))   
        

fire_bat1=Attack_unit('파이어벳',50,16)
fire_bat1.attack('3시')
fire_bat1.damaged(28)
fire_bat1.damaged(28)

class FlyableAttak(Attack_unit,flyable):
    def __init__(self,name,hp,damage,location):
        Attack_unit.__init__(self,name,hp,damage)
        print("{0}:{1} 방향으로 적군을 공격 합니다, [공격력 {2}, 체력{3}]".format(name, location, damage,hp))
        flyable.__init__(self,location)
      
mutal1=FlyableAttak("뮤탈",100,5,10) # 파이썬 내부적으로 mutal1=FlyableAttak("뮤탈",100,5,10)은 Flyableattack(p)로 변환됨
'''

# 스타크래프트 유닛 생성 

# class Unit:
#     def __init__(self,name,hp):
#         self.name=name
#         self.hp=hp
#     # 유닛의 기본틀, 기본정보
    
# class Attack_Unit(Unit):
#     def __init__(self,name,hp,damage):
#         Unit.__init__(self,name,hp)
#         self.damage=damage
#     def attck(self,location):
#         print('{0}:{1}시 방향으로 공격__!'.format(self.name,location))
        
# class Flyable(Attack_Unit,Unit):
#     def __init__(self,name,hp,location):
#         Unit.__init__(self,name,hp)
#         Attack_Unit.attck(self,location)
#     def move(self,location):
#         self.location=location
#         print('{0}:{1}시 방향으로 개같이 이동중'.format(self.name,location))


## 건물생성 / pass 일단 코드가 완성이 안되도 에러없이 실행은 됨
        
# fire_bat1=Attack_Unit('파이어벳',20,8)
# fire_bat1.attck(8)
# Scourge1=Flyable('스커지',5,3)
# Scourge1.move(9)                                    

'''
정학이는 장을 보러 가려고 한
하지만 날씨가 추워 나갈까 말까 고민하고 있다.
오늘의 일기 예보를 보니 18시부터 날씨가 영하로 떨어진다고 한다. 그래서 웬만하면 18시 이전에 장을 보러 가려 한다.

정학이가 출발하는 시간을 입력하면 나갈지 말지 결정하는 프로그램을 작성하라. 시간은 '시간:분' 형태로 입력하며 결과는 'go' 또는 'no'로 출력한다.
'''

'''
name='정학'
time=input('시간을 입력해주세요 \
           ex)12:45 : ')
hour=time[:time.index(":")]
minute=time[-2:]
if int(hour)>=18:
    print("현재시간 : {0}:{1}".format(hour,minute))
    print('오늘은 알몸에이프런이 땡기는 날이야 - {0} -'.format(name))
else: 
    print('오늘은 알몸으로 장을 봐야겠어 - {0} -'.format(name))'''
    
    
    
    


# try:
#     print('나누기 전용 계산기 입니다.')
#     nums=[]
#     nums.append(int(input('첫번째 숫자를 입력하세요 :')))
#     nums.append(int(input('두번째 숫자를 입력하세요 :')))
#     # nums.append(int(nums[0]/nums[1]))
#     print("{0}/{1}={2}".format(nums[0],nums[1],nums[2]))
# except ValueError: # vlaue에 해당하는 오류를 찾아냄
#     print('에러! 잘못된 값을 입력하였습니다.')
# except ZeroDivisionError as err: # as arr로 어떤 오류인지 확인이 가능하다.
#     print(err) 
# # except: # 앞선 오류를 제외하고 명시하지 않은 오류들은 여기서 처리하겠다
# #      print("알 수 없는 에러가 발생하였습니다.")
'''while True:
    try:
        num=int(input('정수를 입력하세요 :'))
    except:
        print('다시 입력하세요')    
    if num==-99:
        print('프로그램이 종료되었습니다.')
        break 
    if str(num)==str(num)[::-1]:
        print('거꾸로 정수입니다.')
    else:
        print('거꾸로 정수가 아닙니다.')'''
        


# num=input('숫자 입력 앙망')
# n_reserve=''
# for char in num:
#     n_reserve=char+n_reserve
# if n_reserve==num:
#     print('거꾸로 숫자')
# else: 
#     print('거꾸로 숫자 아님')
    

# lotto=[]

# for i in range(6):
#     lotto.append(randint(1,46))
#     while i in lotto:
#         lotto.append(randint(1,46))
# print(lotto)

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

'''
while True:
    try:
        num = int(input('定数を入力してください : '))
        if num==-99:
            print('装備を停止致します。')
            break
        if str(num)==str(num)[::-1]:
            print('逆の数字でございます。')
        else:
            print('逆の数字ではありません、ぜひ、もう一度考えた後で入力してください。')  
    except:
        print('ホントのバカなんですか？')
'''

class Unit:
    def __init__(self,name,hp,location):
        self.name=name
        self.hp=hp
        self.location=location
        print('{0}:{1} 유닛생성'.format(name,hp))
    def move(self):
        print('{0}시 방향으로 이동중..'.format(self.location))

fire_bat=Unit('파이어벳',15,0)
fire_bat.move(5)

