# junmin="911122-1234567"

# print("성별 : " + junmin[7])
# print("년 : " + junmin[0:2])
# print("월,일 : " + junmin[2:6])
# print("생년월일 : " + junmin[:6])  # 처음부터 6직전 까지 가져와달라

# print("뒤 일곱자리 : " + junmin[-7:]) # -1이 마지막이다. 그럼 마지막에서 -7번까지를 출력


from itertools import count


site = "http://google.com"
# rull_1=site[7:12]
rull_1 = site.replace("http://","")  # 앞에 http:// 이 부분을 공백으로 replace함
rull_1 = rull_1[:rull_1.index(".")] # 뒤에 .com 부분을 없애기 위해 index로 . 부분을 찾고 .바로 직전만 출력하도록 함
rull_2=rull_1[:3]+str(len(rull_1))+str(rull_1.count('e'))+'!'
print('생성된 패스워드 : {} '.format(rull_2))

