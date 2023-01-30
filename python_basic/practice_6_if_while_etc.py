from random import *
## if 문 

# weather = input("오늘 날씨는 어떻게 되나요? : ")
# if weather == "비" or weather=='눈':  # 조건은 여러개도 줄 수 있다.
#     print("우산을 챙기세여") # 조건에 만족하지 않을 시 아무 문장도 출력되지 않음
# elif weather == "미세먼지":
#     print("put on the mask")
# else :
#     print("don't need a umbrella, mask") #else를 적음으로써 아무조건도 만족하지 않았지만 이 문장이 출력됨
    
# temp = int(input('今日の天気をお知らせいたします。: '))
# if temp >= 30:
#     print('今、出ると亡くなる可能性が高いです。')
# elif temp >= 10 and temp<30:
#     print("ちょうど良い天気です。")
# elif 0 <temp<10: # and 생략하고 이런식으로 표현도 가능함  
#     print('寒いから、コートとかお召しになると暖かくなります。')
# else : 
#     print('あなた、頭がちょっとおかしいですね？')


# ## for, while  반복문
# for Waiting_Number in range(1,6): # 0,1,2,3,4,5 그냥 5만 입력 했을 때 , 1,2,3,4,5/ 시작과 끝을 정한 경우, 1부터 6의 직전까지 출력
#     print('대기번호 : {}'.format(Waiting_Number))
'''
starbucks = {1:'아이언맨', 200:'토르', 12:'스파이더맨', 22:'헐크', 110:'닥스'}
for customer in starbucks:
    print('{0} 손님 커피가 준비되었습니다.'.format(customer))
'''

#while 
# customer = "토르"
# index = 1
# while index <5: # while문에 조건을 준거임
#     print("{0} 손님 커피가 준비되었습니다. {1}번 불렀습니다..".format(customer,index))
#     index+=1
#     if index == 5 :
#         print('정책에 따라 커피를 폐기하겠습니다. 감사합니다 ')

'''
customer = '아이언맨'
index=1
while True: #무한루프임
     print("{0} 손님 커피가 준비되었습니다. {1}번 남았습니다.".format(customer,index))
     index+=1
'''

# customer = '스파이더맨'
# person =''
# while person != customer:
#     print("{0}님 주문하신 아이스아메리카노 나왔습니다.".format(customer))
#     person=input('이름이 어떻게 되세요? : ' )

## continue 와 break   
# absent=[2,5] # 결석
# no_book=[7]

# for student in range(1,11): #1부터 10번까지 책을 읽히게 함
#     if student in absent:
#         continue # 결석자가 있을시 건너뛰어서 읽게함
#     if student in no_book: # 책이 없는 경우
#         print('오늘 수업 여기까지 {0}은 따라나와라 뒤지기 싫으면'.format(student))
#         break
#     print('{0}야, 다음페이지 읽으려무나'.format(student))


## 한줄로 끝내는 for문
'''
v = list(range(10))
print(v)

for i in v:
    print(i)'''


# 비어있는 삼각형
'''
a = int(input("정수를 입력하세요 "))

for i in range(a):
    for k in range(a,i,-1):
        print(' ',end='')

    start = ((i+1)*2-1)
    for k in range(start):
        if k == 0 or k==(start-1) or (i==a-1):
            print("*",end='')
        else:            
            print(" ",end='')
    print()
'''



# lotto=[]
# for i in range(6):
#     j=randint(1,46)
#     while j in lotto: # 리스트안에 j가 한번 더 나올때까지 반복//
#         j=randint(1,46) #참이라면 j변수에 다시 값을 할당한다.
#     lotto.append(j) # 새로운 j값을 추가
# lotto.sort
# print(list(set(lotto)))






lotto=[]
