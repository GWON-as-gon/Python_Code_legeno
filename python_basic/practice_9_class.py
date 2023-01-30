from random import *

# # 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
# name = '마린' # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# # 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있음. 일반 모드/name
# tank_name = '탱크'
# tank_hp = 150
# tank_damage = 35

# tank_name2 = '탱크'
# tank_hp2 = 150
# tank_damage2 = 35

# def attack(name, location, damage):
#     print('{0}:{1} 방향으로 적군을 공격합니다. [공격력 {2}]'.format(\
#         name, location, damage))
# attack('마린','1시',5)
# attack(tank_name,'1시',tank_damage)


# class     init    

#일반 유닛
class Unit:
    def __init__(self, name, hp,speed): #__init__는 파이썬에서의 생성자이다. /객체가 만들어지면 자동으로 호출되는 부분
        self.name=name
        self.hp =hp
        self.speed=speed
        print('{0}유닛이 생성되었습니다.'.format(name))
        
    def move(self, location):
        print('[지상 유닛 이동]')
        print('{0}:{1} 방향으로 이동합니다. [속도 {2}]'.format(self.name, location, self.speed ))
            
    def damaged(self, damage):
        print("{0}:{1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp-=damage
        print("{0}: 현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp<=self.damage:
            print('{0} 유닛이 파괴되었습니다.'.format(self.name))

'''marine1= Unit("마린",40,5) # 클래스로 부터 만들어지는 녀석들은 객체라고 하며, 마린과 탱크는 유닛 클래스의 인스턴스이다.
marine2= Unit("마린",40,5) #self를 제외한 멤버변수와 수가 같아야지 클래스를 통해 인스턴스를 생성할 수 있다.
tank1=Unit('탱크',150,35)

# 레이스 : 공중유닛, 비행기 , 클로킹(상대방에게 보이지 않음)
wraith1=Unit('레이스',80,5)
print('유닛이름 : {0}, 공격력 : {1}'.format(wraith1.name, wraith1.damege))# format함수를 통해 멤버변수에 접근할 수 있다.


# 마인드 컨트롤 :  상대방 유닛을 내 것으로 만드는 것(빼앗음)
wraith2=Unit('빼앗긴 레이스',45,5)
wraith2.clocking=True #클로킹이라는 변수는 클래스 틀에 없다, 하지만 파이썬에서는 외부에다 새로운 변수를 만들어 접근하도록 할 수 있다. 
# 다만 레이스1에서는 접근할 수 없다. 레이스2에만 생성을 했기 때문에, 
# 내가 확장한 객체의 변수에 대해서만 접근을 할 수 있다는 얘기

if wraith2.clocking==True:
    print('{0} 은 지금 클로킹 상태입니다.'.format(wraith2.name))'''
    
# 메소드
## 공격유닛
class Attack_unit(Unit): # 일반 유닛 클래스를 상속 받음
    def __init__(self,name,hp,speed,damage): #클래스내에서 메소드 안에는 self를 항상 적어줘야 함
        #self.name=name                #오른쪽에 있는 name은 전달 받은 값을 쓴다는 얘기이다. self는 자신의 값
        Unit.__init__(self, name, hp, speed) #상속 받은 클래스의 메소드를 명시 해줘야함
        self.damage=damage
        
    def attack(self,location):
        print("{0}:{1} 방향으로 적군을 공격 합니다, [공격력 {2}".format(self.name, location, self.damage))


# 마린
class Marine(Attack_unit):
    def __init__(self):
        Attack_unit.__init__(self,"마린",40,1,5)
        
    # 스팀팩 : 일정시간 동안 이동 및 공격 속도를 증가, 자기 체력 10 감소
    def Stim_Pack(self):
        if self.hp>10:
            self.hp-=10
            print("{0}: 스팀팩을 사용합니다, (HP 10 감소)".format(self.name))
        else: 
            print("{0}: 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))


class Tank(Attack_unit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능, 이동 불가.
    
    
    def __init__(self):
        Attack_unit.__init__(self,'탱크',150,1,35)
        self.seize_mode= False 
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        #현재 시즈모드가 아닐 때 -> 시즈 모드
        if self.seize_mode == False:
            print('{0} : 시즈모드로 전환합니다.'.format(self.name))
            self.damage*2
            self.seize_mode==True
        # 현재 시즈모드 일때 -> 해제
        else:
            print('{0}시즈모드를 해제합니다.'.format(self.name))
            self.damage/2
            self.seize_mode == False
        
# 메딕 : 의무병
'''
# 파이어뱃 : 공격 유닛 , 화염방사기
firebat1=Attack_unit("파이어벳",50,16)
firebat1.attack("5시")
# 공격 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)
'''
## 상속

## 다중 상속
# 드랍쉽 : 공중 유닛, 수송기, (마린, 파이어벳, 탱크), 공격기능x
class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print('{0}:{1} 방향으로 날아갑니다. [속도 : {2}]'\
            .format(name, location, self.flying_speed ))

# 공중 공격 유닛 클래스  
class FlyableAttackUnit(Attack_unit, Flyable):
    def __init__(self,name,hp,damage,flying_speed):
        Attack_unit.__init__(self,name,hp,0,damage) # 지상 스피드는 0 으로 처리
        Flyable.__init__(self,flying_speed)
    
    def move(self, location): #flyable 클래스를 상속하고 있기에 fly함수를 사용할 수 있다. 
        print('[공중유닛이동]')
        self.fly(self.name, location)

# 레이스
class wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,"레이스",80,20,5)
        self.clocked = False # 클로킹 모드 (해제상태)
    
    def clocking(self):
        if self.clocked==True:
            print('{} : 클로킹 모드를 해제합니다.'.format(self.name))
            self.clocked =False
        else: 
            print('{} : 클로킹 모드를 설정합니다.'.format(self.name))
            self.clocked=True
# 발키리 : 공중 공격 유닛 . 한번에 15발 미사일 발사
# valkyrie = FlyableAttackUnit("발키리",200,6,5)
# valkyrie.fly(valkyrie.name,"3시")

## 메소드 오버라이딩
# --> 자식 클래스에서 생성한 메소드를 사용하고 싶을때

#벌쳐
vulture = Attack_unit("벌쳐", 80, 10, 20)

# 배틀 크루저 : 공중유닛
battle_crusiser=FlyableAttackUnit("배틀크루저",500, 25, 3)

vulture.move('11시')
# battle_crusiser.fly(battle_crusiser.name,"9시")
# 이 경우 유닛이 무엇인지 항상 생각하여 무브인지 플라이인지 구분해서 써야함
battle_crusiser.move('9시')

# Pass
## 건물생성 / pass 일단 코드가 완성이 안되도 에러없이 실행은 됨
## 건물 만들거임
'''class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # pass # pass의 의미는 아무것도 안하고 일단은 넘어간다는 뜻읻가.
        # Unit.__init__(self,name,hp,0)
        super().__init__(name,hp,0) #Unit. 이랑 같은 대신 self 생략가능 원하는 인자를 어떤 함수가 가지고 있는지 기억이 안날때 사용하면 유용
        #문제는 다중상속에서 발생
        self.location=location'''
        
        

# 서플라이 디폿 / 인구 증가+8, 1개 = 8유닛
# supply_depot= BuildingUnit("서플라이 디폿",500, "7시")

def game_start():
    print('[알림] 새로운 게임을 시작합니다')
    
def game_over():
    print('Player : gg')
    print('[Player] 님이 게임에서 퇴장하였습니다.')

# 게임시작 
game_start()
# game_over


# super 

# 유닛생성
m1 = Marine()
m2= Marine()
m3 = Marine()

t1=Tank()
t2=Tank()

w1=wraith()

#유닛 일괄 관리(생성된 모든 유닛)
attack_units=[]
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군이동 
for unit in attack_units:
    unit.move("1시")
    
# 탱크 시즈모드 개발
Tank.seize_developed= True
print('[알림] 탱크 시즈 모드 개발이 완료되었습니다.')

# 공격 모드 준비 ()
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.Stim_Pack()
    elif isinstance(unit,Tank):
        unit.set_seize_mode()
    elif isinstance(unit, wraith):
        unit.clocking()

# 전군 공격 
for unit in attack_units:
    unit.attack("1시")

for unit in attack_units:
    unit.damaged(randint(5, 20)) # 공격은 랜덤으로 받음

# 게임 종료
game_over()
    
        

# 공격모드 준비(마린 : 스팀팩, 탱크 : 시즈모드, 레이스 :  클로킹)