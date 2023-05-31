# таукита
def converter(l):
    new = []
    if len(l) % 2 == 0:
        new.append(l.pop(0))
        print(new, l)
        while l:
            new.append(l.pop())
            if len(l) > 0: new.append(l.pop(0))
    else:
        new.append(l.pop())
        while l:
            new.append(l.pop(0))
            if len(l) > 0: new.append(l.pop())
    new.reverse()
    return new

aboba = open("C:/Users/Тимофей/Desktop/олимпиадки/Тау-Кита/input_s1_09.txt").readline().split()
s1 = converter(aboba)
for i in range(len(s1)):
    s2 = []
    s2 += s1[i]
    string = ""
    for l in converter(s2): string += l
    s1[i] = string
    print(string)

ans = open("C:/Users/Тимофей/Desktop/олимпиадки/Тау-Кита/output_s1_09.txt").readline().split()
print(s1 == ans)






# отливка формы
#12 чистых тестов
f = open("C:/Users/Тимофей/Desktop/олимпиадки/формы для отливки/Формы для отливки/input1.txt")
n = int(f.readline())
third = [f.readline()[:-1].split() for i in range(n)]
three = [[third[i][:5], third[i][5:10],third[i][10:15],third[i][15:20]] for i in range(n)]
two = [f.readline()[:-1].split() for i in range(2*n-1)]
two.append(f.readline().split())
second = [[two[i][:5], two[i][5:10], two[i][10:]] for i in range(2*n)]
ans = [(0,0) for i in range(n)]
for i in range(len(two)):
    first = second[i][0]
    last = second[i][-1]
    for j in range(i+1,len(second)):
        if (list(reversed(first)) == second[j][0] and list(reversed(last)) == second[j][-1]) or first == second[j][-1] and last == second[j][0]:#or (list(reversed(first)) == second[j][-1] and list(reversed(last)) == second[j][0])\
            s = [second[j][0], second[j][1],second[j][-1],second[i][1]]
            for h in range(len(three)):
                if (first in three[h] or list(reversed(first)) in three[h]) and (last in three[h] or list(reversed(last)) in three[h]):
                    # print(1.0, i+1, j+1)
                    #if (second[j][1] in three[h] or list(reversed(second[j][1])) in three[h]) and (list(reversed(second[i][1])) in three[h] or second[i][1] in three[h]):
                    # kinda_th = three[h]
                    # kinda_s = s
                    # f = 1
                    three45 = [three[h][1], three[h][2], three[h][3], three[h][0]]
                    three45_2 = [three45[2], three45[3], three45[0], three45[1]]
                    three45_3 = [list(reversed(three45_2[0])), list(reversed(three45_2[-1])), list(reversed(three45_2[2])),
                                  list(reversed(three45_2[1]))]
                    three45_4 = [list(reversed(three45[0])), list(reversed(three45[-1])),
                                  list(reversed(three45[2])),
                                  list(reversed(three45[1]))]
                    three2 = [three[h][2], three[h][3], three[h][0], three[h][1]]
                    three3 = [list(reversed(three2[0])), list(reversed(three2[-1])), list(reversed(three2[2])),
                                  list(reversed(three2[1]))]
                    three4 = [list(reversed(three[h][0])), list(reversed(three[h][-1])),
                                  list(reversed(three[h][2])),
                                  list(reversed(three[h][1]))]
                    threes = [three[h], three2, three3, three4, three45, three45_2, three45_3, three45_4]
                    if [second[j][0], second[j][1], second[j][-1], list(reversed(second[i][1]))] in threes or\
                                [second[j][0], list(reversed(second[i][1])), second[j][-1], second[j][1]] in threes or\
                                [second[i][0], second[i][1], second[i][-1], list(reversed(second[j][1]))] in threes or\
                                [second[i][0], list(reversed(second[j][1])), second[i][-1], second[i][1]] in threes  or\
                                [second[j][0], second[j][1], second[j][-1], second[i][1]] in threes  or \
                                [second[j][0], second[i][1], second[j][-1], second[j][1]] in threes  or \
                                [second[i][0], second[i][1], second[i][-1], second[j][1]] in threes or \
                                [second[i][0], second[j][1], second[i][-1], second[i][1]] in threes: ans[h] = (i+1, j+1)
                        # if [forty[0], forty[1], forty[-1], sixtn[1]] in things or [forty[0], sixtn[1], forty[-1], forty[1]] in things: ...
                        # for k in range(len(kinda_s)):
                        #     if kinda_s[k] in kinda_th:
                        #         for z in range(len(kinda_th)):
                        #             if kinda_th[z] == kinda_s[k]:
                        #                 kinda_th = [kinda_th[g] for g in range(len(kinda_th)) if g != z]
                        #                 break
                        #     elif list(reversed(kinda_s[k])) in kinda_th:
                        #         for z in range(len(kinda_th)):
                        #             if kinda_th[z] == kinda_s[k]:
                        #                 kinda_th = [kinda_th[g] for g in range(len(kinda_th)) if g != z]
                        #                 break
                        #     else:
                        #         f = 0
                        # if f == 1:
                        #     print(1.1," ", i+1, j+1, h+1)
                        #     if i + 1 == 15 and j + 1 == 17: print(three[h],s)
                        #     if i+1 == 15 and j+1 == 34: print(three[h],s)
                        #     ans[h] = (i+1, j+1)
                    # elif list(reversed(first)) in three[h] and list(reversed(last)) in three[h]:
                    #     if second[j][1] in three[h] and second[i][1] in three[h] or list(reversed(second[j][1])) in three[h] and list(reversed(second[i][1])) in three[h]:
                    #         print(1.2," ", i+1,j+1,h)
                    #         ans[h] = (i+1, j+1)

print(*ans)
output = open("C:/Users/Тимофей/Desktop/олимпиадки/формы для отливки/Формы для отливки/output1.txt")
for i in ans:
    s = output.readline().split()
    if(i[0] == int(s[0]) and i[1] == int(s[1])): ...
    else: print("Как должно быть: ",s,"Как есть: ",i)




# обмен денег
f = open("C:/Users/Тимофей/Desktop/олимпиадки/Обмен денег/input14.txt")
reader = [int(i) for i in f.readline().split()]
n1 = reader[0]
begin_currency = []
end_currency = []
for i in range(1,n1):
    begin_currency.append(reader[i])

begin_unfortunate = []
end_unfortunate = []
reader = [int(i) for i in f.readline().split()]
for i in range(1,reader[0]+1):
    begin_unfortunate.append(reader[i])

reader = [int(i) for i in f.readline().split()]
for i in range(1,reader[0]):
    end_currency.append(reader[i])

reader = [int(i) for i in f.readline().split()]
for i in range(1,reader[0]+1):
    end_unfortunate.append(reader[i])
print(begin_unfortunate)
print(begin_currency)
print(end_unfortunate)
print(end_currency)

reader = [int(i) for i in f.readline().split()]
entry = []
out = []
for i in range(len(begin_currency)+1):
    entry.append(reader[i])
print(entry)
# отнимаем несчастл числа
for i in range(len(entry)):
    entry[i] -= sum(1 for x in begin_unfortunate if entry[i] >= x)
# конвертируем в мин ден единицу
if len(entry) > 1:
    while begin_currency:
        entry[1] += entry[0]*begin_currency[0]
        begin_currency.pop(0)
        entry.pop(0)
print("мин",entry)
# конвертируем по всем единицам в другой валюте
while end_currency:
    n = entry[0]
    entry.insert(0, n//end_currency[-1])
    entry[1] = n - entry[0]*end_currency.pop(-1)
print(entry)
# прибавляем в кол-во несчаст чисел
for i in range(len(entry)):
    if entry[i]==640:
        print(1)
        print([x for x in end_unfortunate if entry[i] < x])
    entry[i] += sum(1 for x in end_unfortunate if entry[i] >= x)
ans = open("C:/Users/Тимофей/Desktop/олимпиадки/Обмен денег/output14.txt").readline().split()
for i in range(len(entry)):
    print(entry[i], int(ans[i]))




# Золотая рыбка
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

    
#  XXX Company
chifs = dict()
f = open(f"C:/Users/Тимофей/Desktop/олимпиадки/Компания ХХХ/input_s1_16.txt")
g = open(f"C:/Users/Тимофей/Desktop/олимпиадки/Компания ХХХ/output_s1_16.txt")
s = f.readline()
file = []
while s != "":
    file.append(s.strip())
    s = f.readline()
    # print(file)
target = file[-1]
target_ind = 0

for i in range(0,len(file)-2,2):
    if file[i][:4] not in [x[:4] for x in chifs.keys()]:
        chifs[file[i]] = []
        chifs[file[i]].append(file[i+1])
    else:
        for j in range(len(chifs.keys())):
            if file[i][:4] == list(chifs.keys())[j][:4]:
                chifs[list(chifs.keys())[j]].append(file[i+1])
    if target.isdigit():
        if (file[i][:4] == target): target_ind = i  # только циферную часть смотрим
        if (file[i+1][:4] == target): target_ind = i+1  # только циферную часть смотрим
    else:

        if (file[i][5:] == target): target_ind = i  # только словесную часть смотрим
        if (file[i+1][5:] == target): target_ind = i+1
prev_target_ind = target_ind
keys = list(chifs.keys())
f = 0
for i in range(len(keys)):
    if file[target_ind][:4] == keys[i][:4]:
        target_ind = i
        f = 1
        break
if f:
    recruits = [i for i in chifs[keys[target_ind]]]
    employees = [i for i in chifs[keys[target_ind]]]
    m = ''
    for i in range(len(keys)):
        for j in range(len(chifs[keys[target_ind]])):
            if keys[i][:4] == chifs[keys[target_ind]][j][:4]:
                recruits += chifs[keys[i]]
                if chifs[keys[target_ind]][j].isdigit() and not(keys[i].isdigit()):  recruits[j] = keys[i]
                m = chifs[keys[i]]
                m_prev = [i for i in m]
                while any([m[g][:4] == keys[k][:4] for k in range(len(keys)) for g in range(len(m))]):
                    # print("m",m)
                    for i1 in range(len(keys)):
                        for j1 in range(len(m)):
                                if keys[i1][:4] == m[j1][:4]:
                                    recruits += chifs[keys[i1]]
                                    if m[j1].isdigit() and not (keys[i1].isdigit()):  recruits[j1] = keys[i1]
                                    m_prev = [i for i in m if i != m[j1]]
                                    m = chifs[keys[i1]]
                                    if not(any([m[g][:4] == keys[k][:4] for k in range(len(keys)) for g in range(len(m))])):
                                        m = m_prev
                                        break
    for i in range(len(recruits)):
        if recruits[i].isdigit(): recruits[i] += " Unknown Name"
    recruits.sort()
    reading = [x.strip() for x in g.readlines()]
    print(reading == recruits)
else: print("NO")
