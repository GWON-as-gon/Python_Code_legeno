class SoldOutError(Exception):
    pass

chicken=10
waiting=1
while(True):
    try:
        print('[남은치킨] : {}'.format(chicken))
        order=int(input('치킨은 몇마리로 하시겠습니까? : '))
        if order>chicken:
            print("재료가 부족합니다.")
        elif order<=0:
            raise ValueError
        else: 
            print('[대기번호 {0}] {1}마리 주문이 완료되었습니다.'\
                .format(waiting,chicken))
        if chicken==0:
            raise SoldOutError
        chicken-=order
        waiting+=1
    except ValueError as err: #무슨 에러인지 이유룰 알려줌
        print('잘못된 값을 입력하셨습니다.',err)

    except SoldOutError as err:
        print('재고가 소진되어 더 이상 주문을 받지 않습니다.')
        break 

    finally:  
        print('오늘 하루도 이용해 주셔서 감사합니다.')


