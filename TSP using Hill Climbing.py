import copy

# graph = matrix('0 2 3 3 6; 2 0 4 5 3; 3 4 0 7 3; 3 5 7 0 3; 6 3 3 3 0')
graph = [[0, 2, 3, 3, 6], [2, 0, 4, 5, 3], [3, 4, 0, 7, 3], [3, 5, 7, 0, 3], [6, 3, 3, 3, 0]]
v = 5


def computeCost(path):
    cost = graph[path[0]][path[v - 1]]
    for i in range(v - 1):
        cost += graph[path[i]][path[i + 1]]

    # print(path, cost)
    return cost


def swap(path, p1, p2):
    p = copy.deepcopy(path)
    p[p1], p[p2] = p[p2], p[p1]
    return p


def main():
    initial_path = [0, 1, 2, 3, 4]
    cost1 = computeCost(initial_path)
    print("path =", initial_path, "cost =", cost1)
    # for k in range(1):
    i = 0
    while i < v:
        b = 0
        for j in range(v):
            if i != j:
                new_path = swap(initial_path, i, j)
                cost2 = computeCost(new_path)
                print(new_path, cost2)
                if cost2 < cost1:
                    cost1 = cost2
                    initial_path = new_path
                    print("path =", initial_path, "cost =", cost1)
                    i = 0
                    b = 1
                    break

        if b == 1:
            continue
        else:
            i += 1


if __name__ == "__main__":
    main()
