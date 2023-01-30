# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
# subway1=10
# subway2=20
# subway3=30

# subway = [10,20,30]
# print(subway)
# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# print(subway.index('조세호')) # 조세호가 어느 위치에 있는지 출력

# # 하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append('하하')
# print(subway)

# # 정형돈을 유재석/조세호 사이에 태워 봄
# subway.insert(1,"정형돈")
# print(subway)

# # 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
# print(subway.pop()) # 맨 뒤에서 꺼냄, 꺼냄 사람 출력

# # 같은 이름의 사람이 몇 명 있는지 확인 
# subway.append("유재석")
# print(subway.count('유재석'))

'''
# 정렬도 가능 
num_list = [5,3,1,2,4]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)
'''


#######사전dict#######
# 키에 대한 중복을 허용하지 않는다. "키 콜론 데이터" 형식으로 구성이 됨
# 정수 뿐만 아니라, 문자열도 가능하다.
# cabinet = {3:'유재석',110:'김태호'}
# '''
# print(cabinet[110])
# print(cabinet.get(3))# get 함수를 사용하여 값이 없는걸 출력하려고 하면 none이라고 출력이 된다.
# print(cabinet.get(5,"사용가능"))# 5라는 값은 없지만 none이 출력되지 않고 뒤에 사용가능이라는 말이 출력이 됨
# '''
# print(3 in cabinet)# true
# print(5 in cabinet)# false

# cabinet["c-20"]="조세호"
# print(cabinet)
# cabinet[3]='김종국' # 키 3의 값을 김종국으로 대체하였다.
# print(cabinet)

# # 키 삭제
# del cabinet["c-20"]
# print(cabinet)

# # key 들만 출력
# print(cabinet.keys())

# # values들만 출력
# print(cabinet.values())

# # 키 밸류 둘다 출력
# print(cabinet.items())

# # 목욕탕 폐점
# cabinet.clear()
# print(cabinet)

####튜블#####

# '''
# 1.내용 불가 변경
# 2.속도가 리스트보다 빠름
# 3.그래서 잘 변경되지 않는 경우에 사용
# '''
# menu=('돈까스','치즈까스')
# print(menu[0])
# print(menu[1])

# # menu.add('생선까스') #오류가 남

# # name= '김종국'
# # age=20
# # hobby="코딩"
# # print(name,age,hobby) # 기존에 이렇게 사용한 것을

# # 튜플을 이용시
# (name,age,hobby)=('김종국',20,'운동') # 순서에 맞춰 변수를 선언할 수 있다. 
# print(name,age,hobby)


'''
##### 세트 (집합) #####
# 중복 안됨 , 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {'우원재','넉살','나플라'}
python=set({'넉살','이센스','키드밀리'})
print(java&python) # 자바와 파이썬 모두 할 수 있는 인물
print(java.intersection(python)) # 위와 같은 결과

# 합집합 (java나 python 둘 중에 하나라도 할 줄 아는 사람)
print(java | python)
print(java.union(python))
# 참고로 순서는 무작위로 출력 

# 자바는 할 줄 알지만, 파이썬은 할줄 모르는 사람 (차집합)
print(java-python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어난 경우
python.add('나플라') 
print(python)
print(java-python)
print(java.difference(python)) # 우원재 밖에 남지 않게 됨
java.remove('넉살')
print(java)
'''

# 자료구조의 변경
# 커피숍
menu = {'커피','우유','주스'}
print(menu,type(menu))

menu=list(menu) # 자료구조를 리스트로 바꿈
print(menu,type(menu))

menu=tuple(menu)
print(menu, type(menu))


menu=set(menu)
print(menu,type(menu))
