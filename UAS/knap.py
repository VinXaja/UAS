n = int(input())
kelas = [25, 30, 35]
dp = [[-1 for i in range(kelas[0] + 1)] for j in range(n + 1)]
item = []
for i in range(n):
    name = input()
    weight = int(input())
    priority = int(input())
    item.append([name,weight,priority])
item.sort(key = lambda x : (x[2], x[1]))
print(item)

choice = int(input())
weight = kelas[0]
take = []
total = 0
if choice == 1:
    for i in range(n):
        if weight >= item[i][1]:
            weight -= item[i][1]
            total += item[i][1]
            take.append(item[i][0])
    print(take)
else:
    item.sort(key = lambda x : -(x[1] / x[2]))
    print(item)
    for i in range(n):
        if weight >= item[i][1]:
            weight -= item[i][1]
            total += item[i][1]
            take.append((item[i][0], "WHOLE"))
        elif weight < item[i][1] and weight != 0:
            take.append((item[i][0], f"{weight}/{item[i][1]}"))
            total += weight
            weight -= weight
        print(total)
    print(take)
print(f"ini berapa kg : {total}")
'''
5
Books
10
1
Clothes
12
1
Snacks
4
4
Souvenir
3
2
Cosmetic
1
3

Output
Books
CLothes
Souvenir

1
Books
10
1

5
Books
10
1
CLothes
12
1
Snacks
4
4
Cosmetic
2
2
Souvenir
1
3
'''
