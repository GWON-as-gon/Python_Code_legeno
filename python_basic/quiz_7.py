'''
조건 1: 표준 체중은 별도의 함수 내에서 계산 
    * 함수명 : std_weight
    * 전달값 : 키(height), 성별(gender)
조건2 : 표준 체중은 소수점 둘쨰 자리 까지 표현
'''

height = int(input('본인의 신장을 입력하세요 (cm) :  '))
gender = int(input('성별을 입력하세요 남=1 , 여=2 : '))
    
def std_weight(height,gender):
    if gender ==1 :
        print('적정체중은 {:.2f}입니다'.format(height*height*22/10000))
    else:
        print(height*height*21/10000)

def weight_ret():
    global height

def weight_ret():
    global gender

std_weight(height,gender)

