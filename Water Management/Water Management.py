x,y,z = input().split()

water= 0
price = 0
if x =="ALLOT_WATER":
    if int(y)==3:
        W =1500
        [c,b]=z.split(':')
        c = int(c)
        b = int(b)
        C = c*(W/(c+b))
        B = b*(W/(c+b))
        price +=(C*1 + B*1.5)
    else:
        W =900
        [c,b]=z.split(':')
        c = int(c)
        b = int(b)
        C = c*(W/(c+b))
        B = b*(W/(c+b))
        price +=(C*1 + B*1.5)
water +=W

w=0
try:
    for _ in range(2):
        p,q = input().split()
        if p == 'ADD_GUESTS':
            w += (int(q)*10*30)
    water +=w

    if 0<w<=500:
        price +=(w*2)
        
    elif 500<w<=1500:
        price +=(500*2+(w-500)*3)
        
    elif 1500<w<=3000:
        price +=(500*2 + 1000*3 +(w-1500)*5)
        
    else:
        price +=(500*2 + 1000*3 +1500*5 +(w-3000)*8)
except:
    pass
    

print(water, price)