from numpy import *
import copy

final = array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
initial = array([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
#final = matrix('1, 2, 3; 8, 0, 4; 7, 6, 5')
#initial = matrix('2, 8, 3; 1, 6, 4; 7, 0, 5')
#final = final.reshape(3, 3)
#initial = initial.reshape(3, 3)
a = 10


def display(state):
    for i in range(3):
        for j in range(3):
            print(state[i][j], end=" ")
        print()
    print("======")


def cost(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != final[i][j]:
                count += 1
    return count


def findBlank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def up(s, i, j):

    state = copy.deepcopy(s)
    print("state[i-1,j]",state[i-1][j])
    #try:
    state[i,j], state[i - 1,j] = state[i - 1,j], state[i,j]
    #except:
     #   print("h")
      #  pass
    return state


def down(s, i, j):
    state = copy.deepcopy(s)
    #try:
    state[i,j], state[i + 1,j] = state[i + 1,j], state[i,j]
    #except:
     #   print("h")
      #  pass
    return state


def left(s, i, j):
    state = copy.deepcopy(s)
    #try:
    state[i,j], state[i,j + 1] = state[i,j + 1], state[i,j]
    #except:
     #   print("h")
      #  pass
    return state


def right(s, i, j):
    state = copy.deepcopy(s)
    #try:
    state[i,j], state[i,j - 1] = state[i,j - 1], state[i,j]
    #except:
     #   print("h")
      #  pass
    return state


current = copy.deepcopy(initial)
count = cost(initial)
display(initial)

while count != 0:
    c = list()
    i, j = findBlank(current)
    print(i,j)

    try:
        s0 = up(current, i, j)
        print(s0)
        c.append(cost(s0))
    except:
        print("h")

    try:
        s1 = down(current, i, j)
        print(s1)
        c.append(cost(s1))
    except:
        print("h")

    try:
        s2 = left(current, i, j)
        print(s2)
        c.append(cost(s2))
    except:
        print("h")

    try:
        s3 = right(current, i, j)
        print(s3)
        c.append(cost(s3))
    except:
        print("h")

    print(c)

    count = min(c)
    pos = c.index(count)
    if pos == 0:
        current = s0
    elif pos == 1:
        current = s1
    elif pos == 2:
        current = s2
    else:
        current = s3

    print(type(current),current)
    print(count)