Q = [3, 16, 14, 7, 5, 8, 16]
Q = [8, 15, 3, 7]
Q = [15, 11, 5, 14, 13, 12, 20, 10, 20]
# 20+11+20+13+5
# 15+10+12+14
def maxCoins(Q):
        # Code here
    q = Q.copy()

    x,X = 0,0
    y,Y = 0,0

    x +=Q[0]
    Q.remove(Q[0])
    while len(Q) > 0 :
        try:
            if Q[0] >= Q[len(Q)-1]:
                y += Q[0]
                Q.remove(Q[0])
            else:
                y +=Q[len(Q)-1]
                Q.remove(Q[len(Q)-1])

            if Q[0] < Q[len(Q)-1]:
                x +=Q[len(Q)-1]
                Q.reverse()
                Q.remove(Q[0])
                Q.reverse()
            else:
                x += Q[0]
                Q.remove(Q[0]) 
        except:
            pass       
 

    X +=q[len(q)-1]
    q.reverse()
    q.remove(q[0])
    q.reverse()
    while len(q)>0:
        try:
            if q[0] >= q[len(q)-1]:
                Y += q[0]
                q.remove(q[0])
            else:
                Y += q[len(q)-1]
                q.reverse()
                q.remove(q[0])
                q.reverse()

            if q[0] < q[len(q)-1]:
                X +=q[len(q)-1]
                q.reverse()
                q.remove(q[0])
                q.reverse()
            else:
                X += q[0]
                q.remove(q[0])
        except:
            pass          

    if X>x:
        if X>Y:
            result = X
        else:
            result = Y
    else:
        if x>y:
            result = x
        else:
            result = y
    return result        
        
print(maxCoins(Q))