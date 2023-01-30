import sys # 표준출력으로 출력할지, 표준에러로 처리할지 정할 수 있음
# print('python','java', sep='vs', end='?') # sep는 콤마 사이에 원하는 말을 집어넣을수있다. # end는 문장의 끝부분을 줄바꿈 대신 원하는 말로 대체해라 라는 의미이다. 
# print('무엇이 더 재미있을까요?')

# print('python', 'java', file=sys.stdout)
# print('python', 'java', file=sys.stderr)
import pickle

'''scores = {'수학':0, '영어':50, '코딩':100}
for subject, score in scores.items(): # 키와 밸류를 쌍으로 과목과 점수에 보내줄 수 있다.
    # print(subject,score)
    print(subject.ljust(8), str(score).rjust(5), sep=':') #ljust왼쪽으로 정렬 그리고 옆으로 8칸 띄우기, rjust 오른쪽 정렬 그리고 5칸 띄우기
'''
'''
# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1,21):
    print('대기번호 :', str(num).zfill(3))
'''

'''
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬응 하되, 총 10 자리 공간을 확보
print('{0: >10}'.format(500))
print('{0: >+10}'.format(500))
print('{0: >+10}'.format(-500))
# 왼쪽 정렬하고, 빈칸으로 _를 채움
print('{0:_<10}'.format(500))
# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000000))
print("{0:+,}".format(100000000000))
print("{0:,}".format(-100000000000))
# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# 돈이 많으면 기분이 좋으니 빈 자리는 ^로 채우기
print("{0:ㅎ<+30,}".format(10000000000))
#소수점 출력
print('{0:.2f}'.format(3.145641231)) # 반올림해서 소수점 2자리까지 출력
'''
# 파일 입출력 
# score_file=open('score.txt','w',encoding='utf8') # 오픈을 통해 파일을 열고, w로 쓰기위한 파일이란 명시,utf한글깨짐 방지
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()# 파일을 열면 항상 닫아줘야함 

# score_file=open('score.txt', 'a', encoding='utf8') # a는 append의 약어로 파일을 덮어쓰는게 아닌 기존 파일에 계속해서 쓰겠다는 소리다.
# score_file.write('과학 : 80')
# score_file.write('\n코딩 : 100') #print문과 다르게 자동개행이 되지 않기에 탈출문자를 써줘야 함
# score_file.close()

# score_file=open('score.txt','r',encoding='utf8') # 파일을 읽기만 하는 경우
# print(score_file.read())
# score_file.close()

# score_file= open('score.txt','r',encoding='utf8')
# print(score_file.readline(),end='') #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(),end='') 
# print(score_file.readline(),end='') 
# print(score_file.readline(),end='') 
# score_file.close()

# # 만약 파일에 줄이 몇줄인지 모를때
# score_file= open('score.txt','r',encoding='utf8')
# while True:
#     line=score_file.readline()
#     if not line:
#         break
#     print(line,end='')
# score_file.close()
    

#pickle
# 프로그램에 있는 데이터를 파일형태로 저장하는 것
# 파일을 누군가에보내면 눈군가는 다시 그파일을 피클로 재사용 가능
# profile_file = open('profile.pickle', "wb")#W쓰기, b= Binary 파일 피클은 항상 바이너리를 지정해줘야함
# profile={'이름':'박명수','나이':30, "취미":['축구','골프','코딩 ']} #피클은 만들었고 실제 들어가는 데이터
# print(profile)
# pickle.dump(profile,profile_file)#Profiled에 있는 정보를 FILE에 저장
# profile_file.close()

# profile_file = open('profile.pickle', "rb")
# profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()


# #with
# with open('profile.pickle','rb') as profile_file:
#     print(pickle.load(profile_file)) #file close를 사용하지 않아도 됨

# with open('study.txt', 'w', encoding='utf8') as study_file: # 바이너리 지정 하지 않아도 됨
#     study_file.write("파이썬을 열심히 공부하고 있어요") #두줄에 걸쳐서 파일 생성이 가능함

# with open('study.txt', 'r', encoding='utf8') as study_file:
#     print(study_file.read())


