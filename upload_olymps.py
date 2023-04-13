f = open("C:/Users/Тимофей/Desktop/олимпиадки/Золотая рыбка/input_s1_02.txt")
n = int(f.readline())
magic = []
for i in range(n): magic.append(f.readline()[:-1])
first = int(f.readline())
d_f = {}
for i in range(first):
    r = f.readline().split()
    k = r[0]
    v = int(r[1])
    d_f[k] = v
last = int(f.readline())
d_l = {}
for i in range(last):
    r = f.readline().split()
    k = r[0]
    v = int(r[1])
    d_l[k] = v
m = c = 0
def normal(magic,first,last):
    c = 0
    m = [i for i in magic]
    f = {x[0]:x[1] for x in first.items()}
    l = {x[0]:x[1] for x in last.items()}
    while (True):
        flag = 0
        for i in range(len(m)):
            if m[i][0] in f.keys() and m[i][-1] in l.keys():
                c += 1
                l[m[i][-1]] -= 1
                f[m[i][0]] -= 1
                # print(m[i], f[m[i][0]], l[m[i][-1]])
                if f[m[i][0]] == 0: f.pop(m[i][0])
                if l[m[i][-1]] == 0: l.pop(m[i][-1])
                flag = 1
                m.pop(i)
                break
        if flag == 0: break
    return c
def rev(magic,first,last):
    c = 0
    m = [i for i in magic]
    f = {x[0]:x[1] for x in first.items()}
    l = {x[0]:x[1] for x in last.items()}
    while (True):
        flag = 0
        for i in reversed(range(len(m))):
            if m[i][0] in f.keys() and m[i][-1] in l.keys():
                c += 1
                l[m[i][-1]] -= 1
                f[m[i][0]] -= 1
                # print(m[i], f[m[i][0]], l[m[i][-1]])
                if f[m[i][0]] == 0: f.pop(m[i][0])
                if l[m[i][-1]] == 0: l.pop(m[i][-1])
                flag = 1
                m.pop(i)
                break
        if flag == 0: break
    return c
def unique(magic,first,last):
    c = 0
    m = [i for i in magic]
    f = {x[0]: x[1] for x in first.items()}
    l = {x[0]: x[1] for x in last.items()}
    curr = []
    while (True):
        flag = 0
        for i in range(len(m)):
            if m[i][0] in f.keys() and m[i][-1] in l.keys() and (m[i][0]+m[i][-1]) not in curr:
                c += 1
                l[m[i][-1]] -= 1
                f[m[i][0]] -= 1
                # print(m[i][0]+m[i][-1],curr)
                curr.append(m[i][0]+m[i][-1])
                # print(m[i], f[m[i][0]], l[m[i][-1]])
                if f[m[i][0]] == 0: f.pop(m[i][0])
                if l[m[i][-1]] == 0: l.pop(m[i][-1])
                flag = 1
                m.pop(i)
                break
        if flag == 0 and curr == []: break
        elif flag == 0:
            # print(curr)
            curr = []

    return c
def Maks(magic,first,last):
    c = 0
    m = [i for i in magic]
    f = {x[0]: x[1] for x in first.items()}
    l = {x[0]: x[1] for x in last.items()}
    concat = dict()
    for k1, v1 in f.items():
        for k2, v2 in l.items(): concat[k1 + k2] = v1 + v2
    concat = dict(sorted(concat.items(), key=lambda item: item[1]))
    for k in reversed(concat.keys()):
        delete = []
        for i in range(len(m)):
            if m[i][0] == k[0] and m[i][-1] == k[-1] and f[k[0]] > 0 and l[k[1]] > 0:
                c += 1
                # print(magic[i], d_f[k[0]], d_l[k[-1]],c)
                f[k[0]] -= 1
                l[k[1]] -= 1
                # print(k)
                delete.append(i)
        delete.sort(reverse=True)
        while delete:
                # print("deleting",delete,m)
            m.pop(delete.pop())
            delete = [i - 1 for i in delete]
    return c
print(max(normal(magic,d_f,d_l),rev(magic,d_f,d_l),unique(magic,d_f,d_l),Maks(magic,d_f,d_l)))

# Рубик Кубика
f = open("C:/Users/Тимофей/Desktop/Кубик Рубика/input_s1_20.txt")
n, m = map(int, f.readline().split())
first = tuple(int(i) for i in f.readline().split())
x = first[0]
y = first[1]
z = first[2]
moves = [f.readline().split() for i in range(m)]
for i in range(len(moves)):
    letter = moves[i][0]
    digit = int(moves[i][1])
    direction = int(moves[i][2])
    p_x = x
    p_y = y
    p_z = z
    if letter == "X" and x == digit:
        if direction > 0:
            temp = z
            z = n + 1 - y
            y = temp
        if direction < 0:
            temp = y
            y = n + 1 - z
            z = temp
    elif letter == "Y" and y == digit:
        if direction > 0:
            temp = z
            z = n + 1 - x
            x = temp
        if direction < 0:
            temp = x
            x = n + 1 - z
            z = temp
    elif letter == "Z" and z == digit:
        if direction > 0:
            temp = y
            y = n + 1 - x
            x = temp
        if direction < 0:
            temp = x
            x = n + 1 - y
            y = temp
g = open("C:/Users/Тимофей/Desktop/Кубик Рубика/output_s1_20.txt")
ans = list((int(i) for i in g.readline().split()))
if ans[0] == x and ans[1] == y and ans[2] == z: print("YES")
else:
    print("Должно быть: ",ans)
    print("Как есть: ",x,y,z)
    
    
# зелье
f = open("C:/Users/Тимофей/Desktop/олимпиадки/Зельеварение/Зельеварение/input10.txt")
s = f.readline()
recept = {"DUST":["DT","TD"], "FIRE":["FR","RF"], "WATER":["WT","TW"], "MIX":["MX","XM"]}
file = []
while(s != ""):
    file.append(s.strip().split())
    sp = ""
    s = f.readline()
spells = [[] for i in range(len(file))]
for i in range(len(file)):
    spells[i] = recept[file[i][0]][0]
    for j in range(1,len(file[i])):
        if not(file[i][j].isdigit()): spells[i] += file[i][j]
        else: spells[i] += spells[int(file[i][j])-1]
    spells[i] += recept[file[i][0]][1]
g = open(f"C:/Users/Тимофей/Desktop/олимпиадки/Зельеварение/Зельеварение/output10.txt")
out = g.readline()
if out == spells[-1]: print("GOOD")
else: print(f"Как есть: {spells[-1]},как должно быть: {out}")
