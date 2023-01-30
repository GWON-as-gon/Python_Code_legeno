import math 
global number
number=0

def reform_ip_bin(ip:str):
    Ip=ip
    bin_ip_list=ip.split('.')
    for i in range(len(bin_ip_list)):
        length=len(bin((int(bin_ip_list[i])))[2:])#'str' object cannot be interpreted as an integer so reform to int
        bin_ip_list[i]=('0'*(8-length))+bin((int(bin_ip_list[i])))[2:]# reform 8numbers bin  ex 1100 -> 00001100
    bin_ip=''.join(bin_ip_list)
    return bin_ip


def networkid(ip:str,prefix:int):
    network_bin=reform_ip_bin(ip)
    ipbin=network_bin[:prefix]+('0'*len(network_bin[prefix:]))
    ipbin=list(map(''.join, zip(*[iter(ipbin)]*8)))
    networkid_list=[]
    for i in ipbin:
        networkid_list.append(str(int(i,2)))
    print(networkid_list)
    return networkid_list

def lanlist(ip_list:str,sizeoflan):
    sizeoflan_bin=bin(sizeoflan)[2:]
    result=bin(int(reform_ip_bin(ip_list),2)+int(sizeoflan_bin,2)-1+number)[2:]
    
    result=('0'*(32-len(result)))+result
    result=list(map(''.join,zip(*[iter(result)]*8)))
    
    for i in range(len(result)):
        result[i]=str(int(result[i],2))
    
    result='.'.join(result)
    
    return result
    
    
#def rest_ip_numbers(ip:str,prefix:int):
    
    
ip=input('ip 범위: ')
prefix=int(input('프리픽스: '))
networkidlist=networkid(ip,prefix)
remained_ip=(2**(32-prefix))-2
print('사용가능한 ip 개수' + str(remained_ip))
print('-----------------------------------------------------------------------------------------')
networkids='.'.join(networkidlist)
numberoflan=int(input('lan 개수:'))
for i in range(numberoflan):
    numbersofip=int(input('사용할 ip 개수: '))
    sizeoflan=2**(math.ceil(math.log2(numbersofip)))
    print('최소 lan 크기: ',sizeoflan)
    remained_ip=remained_ip-sizeoflan
    print('남은 ip 개수수:',remained_ip)
    print('ip 범위',networkids+'~'+lanlist(networkids,sizeoflan))
    number+=1
    networkids=lanlist(networkids,sizeoflan)
    if remained_ip <=0:
        print('ip 개수 부족 ')
        break 