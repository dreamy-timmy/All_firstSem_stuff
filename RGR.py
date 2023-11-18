#here we gonna do some main stuff


def algorithm():
    # используем алгоритм Дейкстра с добавлением 1 часа при пересадке (если пункт не  конечен, т.е. не равен 1)
    I = [1, 2, 3, 4, 5, 6, 7]
    ribs = [[2, 1], [3, 1], [4, 1], [4, 3], [5, 4], [6, 2], [6, 3], [7, 1], [7, 2], [7, 3],
            [7, 5], [7, 6]]
    weight = [3, 2, 9, 8, 7, 3, 5, 25, 15, 11, 5, 10]
    # прибавляем по 1 к весам промежуточных остановок (время пересадки)
    for i in range(len(ribs)):
        if ribs[i][1] != 1: weight[i] += 1
    # дальше идёт собственно сам алгоритм
    tops = set()
    sm = 0
    s = [None for i in range(len(I))]
    # указываем начальную вершину и присваеваем ей значение 0
    tops.add(I[6])
    s[I[6] - 1] = 0
    current = []
    top = I[6]
    ind = -1
    delete = []
    while ribs:
        if ind + 1 <= len(ribs) - 1:
            ind += 1
        else:
            if current:
                mn = s[current[0] - 1]
                t = current[0]
                for j in range(len(current)):
                    if mn > s[current[j] - 1]:
                        t = current[j]
                        mn = s[current[j] - 1]
                tops.add(t)
                top = t
                current = []
                ind = 0
                delete.sort(reverse=1)
                while delete:
                    ribs.pop(delete[0])
                    weight.pop(delete[0])
                    delete.pop(0)
            else:
                for i in range(len(I)):
                    if I[i] not in tops:
                        top = I[i]
                        print(top)
                        tops.add(top)
                        break
        if weight and top == ribs[ind][0]:
            if s[ribs[ind][1] - 1]:
                s[ribs[ind][1] - 1] = min(s[ribs[ind][0] - 1] + weight[ind], s[ribs[ind][1] - 1])
            else:
                s[ribs[ind][1] - 1] = s[ribs[ind][0] - 1] + weight[ind]
            current.append(ribs[ind][1])
            delete.append(ind)
        elif weight and top == ribs[ind][1]:
            if s[ribs[ind][0] - 1]:
                s[ribs[ind][0] - 1] = min(s[ribs[ind][1] - 1] + weight[ind], s[ribs[ind][0] - 1])
            else:
                s[ribs[ind][0] - 1] = s[ribs[ind][1] - 1] + weight[ind]
            current.append(ribs[ind][0])
            delete.append(ind)
    print(
        f'{s[0]} - наименьшее кол-во часов, которое пассажир может провести при полёте на самолёте от Владивостока до Анкары')
def author():
    print("Автор: \nТимофей Вячеславович Гюнтер\nФИТ-221")

while(True):
    print("1) Посмотреть результат работы - минимальное кол-во часов")
    print("2) Об авторе")
    print("3) Выход")
    menu = 0
    while (menu not in [1,2,3]):
        try:
            print()
            menu = int(input("Ваши действия: "))
        except:
            print("Норм вводи!!")
    if menu == 1: algorithm()
    elif menu == 2: author()
    else: break







