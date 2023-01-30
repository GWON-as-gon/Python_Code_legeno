'''
def sample_accout() :
    print("새로운 계좌가 생성되었습니다. ")
# 함수는 정의만 해두는 것이지 실제로 호출을 하기 전까지 실행이 되지 않는다. 

sample_accout()# 호출

## 전달값과 반환값

def deposit(balance, money) : #입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance + money

def withdraw(balance, money) : #출금
    if balance >= money: # 잔액이 출금보다 많음녀
        print('출금이 완료되었습니다. 남은 금액은 {0}원 입니다.'.format(balance-money))
        return balance-money
    else :
        print("잔액이 부족합니다. 다시 금액을 입력하세요")
        return balance
   
    
balance = 0 # 잔액
balance = deposit(balance,1000)
print(balance)

withdraw(balance,200)

def withdraw_night(balance, money):
    commision = 100 # 수수료
    return commision, balance-money-commision

balance = 0 # 잔액
balance = deposit(balance,1000)
commision, balance = withdraw_night(balance, 500)
print('출금이 완료되었습니다. 수수료는 {0}원이며, 잔액은 {1}원 입니다.'.format(commision, balance))
'''

####기본값#####
'''
def profile(name, age, main_lang):
    print('이름 : {0} \n나이 : {1} \n주 사용 언어 :{2}\n'\
        .format(name, age, main_lang))

profile('유재석', 18, 'java')
profile('김태호',17,'python')
'''
'''
# 같은 학교 같은 반 같은 수업일 경우
def profile(name, age=17, main_lang='python'):
    print('이름 : {0} \n나이 : {1} \n주 사용 언어 :{2}\n'\
        .format(name, age, main_lang))

profile('김태호')
profile('유재석')
'''
'''
## 키워드 값
def profile(name, age, language):
    print(name,age,language)

profile(name='유재석', language='java', age=24)
profile(age=24,name='김태호',language='python')
# 순서가 뒤섞여있어도 함수를 호출 할 수 있다.
'''

## 가변인자
'''def profile(name, age, lang1, lang2, lang3, lang4):
    print('이름 : {0}\n나이 : {1}\n'.format(name,age), end=" ")
    print(lang1,lang2,lang3,lang4) 3. 이러한 상황을 대비하기 위해 가변인자가 만들어짐
'''
'''
def profile(name, age, *language): # 내가 넣고 싶은 만큼 언어를 넣겠다고 명시함
    print('이름 : {0}\n나이 : {1}\n'.format(name,age), end=" ")# 줄바꿈을 하지 않기 위해 뒤에 end 를 추가함
    for lang in language:
        print(lang,end=' ')
    print()


profile('유재석', 24, 'java','python', 'java_script', 'php', 'c##', 'C++') #1.언어가 한개 더 추가가 되었을 경우는 어떻게 해야함?
profile('김태호', 20, 'kotlin','swift') # 2.이러한 방식은 손이 너무 많이 감 

'''

## 지역변수와 전역변수
# 지역변수는 함수내에서만 쓸 수 있다. 함수 호출이 끝나면 사라지는 것
# 전역변수는 언제 어디서든 부를 수 있는 것
gun=10

def checkpoint(soldiers): # 경계근무
    global gun
    gun= gun-soldiers  
    print('[함수 내] 남은 총 : {0}'.format(gun))

def checkpoint_ret(gun,soldiers):
    gun  = gun-soldiers
    print('[함수 내] 남은 총 : {0}'.format(gun))
    return gun # 여기서 바뀐 건의 값을 리턴하여 외부로 던질 수가 있음


print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun,2)
#checkpoint(2) # 2명의 경계 근무 나감
print("전체 총 : {0}".format(gun))# 함수 외부에 있는 gun의 값은 전혀 변하지 않음, 이럴 경우에 사용하는 것이 전역 변수
# 일반적으로는 전역변수를 많이 쓰면 함수 관리가 어려우니 주의해서 사용하자

