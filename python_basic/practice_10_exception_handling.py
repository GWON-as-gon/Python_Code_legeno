'''# 예외처라
## 자료형을 잘못 전달 받았을때의 경우
try:
    print('나누기 전용 계산기 입니다.')
    nums=[]
    nums.append(int(input('첫번째 숫자를 입력하세요 :')))
    nums.append(int(input('두번째 숫자를 입력하세요 :')))
    # nums.append(int(nums[0]/nums[1]))
    print("{0}/{1}={2}".format(nums[0],nums[1],nums[2]))
except ValueError: # vlaue에 해당하는 오류를 찾아냄
    print('에러! 잘못된 값을 입력하였습니다.')
except ZeroDivisionError as err: # AS를 치면 프린터에 똑같은 말 출력도 가능
    print(err) 
# except: # 앞선 오류를 제외하고 명시하지 않은 오류들은 여기서 처리하겠다
#      print("알 수 없는 에러가 발생하였습니다.")

except Exception as err:
    print(err) # 리스트를 벗어났다는 말이 출력됨'''
    
class BigNumberError(Exception):
    def __init__(self,msg):
        self.msg=msg
        
    def __str__(self):
        return self.msg
    
# error 발생시키기
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2>=10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1,num2))
    print("{0}/{1}={2}".format(num1,num2,int(num1/num2)))
except ValueError:
    print('잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요 ')
except BigNumberError as err:
    print('잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요 ')
    print(err)
finally:
    print("계산기를 이용해주셔서 감사합니다.")

#Finally
## 예외처리가 발생하든 아니든 무조건 실행되는 구문




