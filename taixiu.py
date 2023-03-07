import random
import time
def xoaysucxac():
    a = random.randint(1,6)
    b = random.randint(1,6)
    c = random.randint(1,6)
    ans = [a, b, c]
    return(ans)
def nhapdapan():
    while True:
        a = input('moi nhap 1-6, tai, xiu:')
        try:
            a = int(a)
            if a>=1 and a<=6:
                break
            else:
                print('ban nhap sai moi nhap lai')
            
        except:
            if a == 'tai' or a == 'xiu' or a == 'end':
                break
            else:
                print('ban nhap sai moi nhap lai')
    return a
def sosanhketqua(lst, ans):
    if type(ans) == int:
        dem = 0
        for i in lst:
            if ans == i:
                dem+=1
        return dem
    elif type(ans) == str:
        
        tong = sum(lst)
        if tong <= 10:
            kq = 'xiu'
        elif tong >= 11:
            kq = 'tai'
        if ans == kq:
            return 1
        else:
            return 0
def nhaptiencuoc(tien):
    while True:
        n = input('moi nhap tien cuoc:')
    
        try:
            n = int(n)
            if n < 0 or n > tien:
                print('so tien khong hop le')
            else:
                break
        except:
            if n == 'all in':
                n = tien
                break
            elif n == 'end':

                break
            else:
                print('so tien khong hop le')
    return n
def inraxucsac(lst):
    print('suc sac 1:', lst[0])
    time.sleep(0.5)
    print('suc sac 2:', lst[1])
    time.sleep(0.5)
    print('suc sac 3:', lst[2], '''
    ''')
    print('tong bang:', sum(lst))
tien = 1000
while True:
    lst = xoaysucxac()
    ans = nhapdapan()
    if ans == 'end':
        break
    tiencuoc = nhaptiencuoc(tien)
    if tiencuoc == 'end':
        break
    kq = sosanhketqua(lst, ans)
    if kq == 0:       
        tien = tien-tiencuoc        
        inraxucsac(lst)
        print('you lose')
        print(tien)   
    else:
        inraxucsac(lst)
        print('you win')     
        tien = tien+(tiencuoc*kq)
        print(tien)
        