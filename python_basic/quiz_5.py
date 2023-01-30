import random

'''
조건 1 : 편의상 댓글은 20명이 작성 아이디는 1~20이라고 가정
조건 2 : 댓글 내용과 상관없이 무작위로 추첨 중복 불가
조건 3 : random 모듈의 shuffle과 샘플 활용
'''

'''
(출력예제)
--당첨자 발표--
치킨 당첨자 : 1
커피 당첨자 : [2,3,4]
--축하 합니다!--
'''

id = list(range(1,20))
random.shuffle(id)
atari=random.sample(id,4)
print('''
      --당첨자 발표--
      치킨 당첨자 : {}
      커피 당첨자 : {}
      --축하 합니다--
      '''.format(atari[0],atari[1:])
      )