from random import *
'''quiz
당신은 cocoa 서비스를 이용하는 기사님입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오

조건 1: 승객별 운행 소요 시간은 5분~50 사이의 난수로 정해집니다.
조건 2: 당신은 소요 시간 5분~15분 사이의 승객만 매칭해야 합니다.
'''
'''
Customer=range(50)
Cus_time=range(5,50)
index=1
count=0 # 총 탑승 승객 수

for driver in Customer:
    Cus_time = randrange(5,51)
    if Cus_time>15 :
        print('[ ] {0}번째 손님 (소요시간 : {1}분'.format(index,Cus_time))
        index+=1
    else :
        print('[O] {0}번째 손님 (소요시간 : {1}분'.format(index,Cus_time))
        index+=1
        count+=1
        

print('총 탑승 승객 : {0} 분'.format(count))


for i in range(100):
    if i%2!=0:
        print(i, end=' ')
print()
'''

'''
i=[1,2,3,4,5,6,7,8,9]

for i in i:
    for j in range(9):
        j+=1
        num=i*j
        print('{0}*{1}={2}'.format(i,j,num), end=" ")
'''



st='*'
num = int(input('숫자를 입력하세요 : '))
for i in range(num):
    for k in range(num):
        print(' ',end='')
    num-=1
    for j in range((i)*2-3):
        print(st,end='')
    print()
    

