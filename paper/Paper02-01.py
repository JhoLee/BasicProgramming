'''
<단순 변수 사용>
    2. 선택형
    2-1. 홀수와 짝수 판별식으로, 홀수 짝수 판별
    1626035 이주호
'''

#판별할 정수 입력
num = int(input("판별할 정수 입력 >> "))

#홀수 짝수 판별
if(num % 2 == 0):
    print("%d는 짝수입니다." % num)
if(num % 2 != 0):
    print("%d는 홀수입니다." % num)