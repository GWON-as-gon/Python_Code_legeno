class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("flyable 생성자")

class FlyableUnit(Unit,Flyable):
    def __init__(self):
        super().__init__()

# 드랍쉽
## 2개 이상의 클래스를 상속 받을 경우, super는 첫번째 인자에 있는 클래스만 불러온다

dropship = FlyableUnit()