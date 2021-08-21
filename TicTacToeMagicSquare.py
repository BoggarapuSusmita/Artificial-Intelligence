from itertools import *

sq={1:{8:'_',3:'_',4:'_'},
    2:{1:'_',5:'_',9:'_'},
    3:{6:'_',7:'_',2:'_'}}
win='N'
count=0

#printing board
def board():
    for i in sq:
        for j in sq[i]:
            print(j, sq[i][j], end="   ")
        print()

#get key values
def getKeys(p):
    key = []
    for i in sq:
        for j in sq[i]:
            if (sq[i][j] == p):
                key.append(j)
    return key

#check winning condition
def winning(p):
    key = getKeys(p)
    comb = combinations(key, 3)
    for i in comb:
        s=sum(list(i))
        if s==15:
            return p
    return 'N'

#check block condition
def check(p1,p2):
    key=getKeys(p1)
    comb=combinations(key,2)
    for i in comb:
        s=sum(list(i))
        next=15-s
        if next>0 and next<=9:
            for k in sq:
                if next in sq[k].keys() and sq[k][next]=='_':
                    sq[k][next]=p2
                    return 1
    return 0

#computer enters at random place
def random():
    for i in sq:
        for j in sq[i]:
            if sq[i][j]=='_':
                sq[i][j]='X'
                break
        else:
            continue
        break

while win=='N' and count<9:
    c=0
    c=check('X','X')
    if c==0:
        c=check('O','X')
    if c==0:
        random()
    board()
    win=winning('X')
    count+=1
    if count>=9 or win=='X':
        break

    #USER INPUT
    user=int(input("enter next position"))
    for i in sq:
        if user in sq[i].keys():
            sq[i][user]='O'
            break
    count += 1
    win=winning('O')

if win=='N':
    print("MATCH DRAWN")
elif win == 'X':
    print("X WON")
elif win == 'O':
    board()
    print("O WON")