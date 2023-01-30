'''
출력 예제
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년
'''



class House:
    def __init__(self, location, house_type, deal_type, price,completion_year):
        self.location=location
        self.house_type=house_type
        self.deal_type=deal_type
        self.price=price
        self.completion_year=completion_year
    

    def show_detail(self):
        print('{} {} {} {} {}년'.format(self.location,self.house_type,self.deal_type,self.price,self.completion_year))


home=[]  
apt=House('강남','아파트','매매','2억',2010)
op=House('마포','오피스텔','전세','5억',2007)
bil=House('송파','빌라','월세','500/50',2000)
home.append(apt)
home.append(op)
home.append(bil)

print('총 {}대의 매물이 있습니다.'.format(len(home)))
for house in home:
    house.show_detail()