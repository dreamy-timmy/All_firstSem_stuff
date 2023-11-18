# можно создавать выступление, задавать его тему, время его начала и длительность.
# Программа должна следить за тем,
# чтобы доклады не перекрывались во времени и предупреждать пользователя,
# если это произошло; выводить суммарное время доклада, время самого продолжительного перерыва между докладами и так далее.
# Надо реализовать два класса: «доклад» и «конференция».
# Как распределить между ними функциональность, решать Вам. Программа должна иметь хороший интерфейс с подсказками, что нужно вводить.

class Presentation:
    counter = 0
    duration = 1  # по умолчанию 1 час
    summary_time = 0
    def __init__(self,name,conf_name):
        Presentation.counter += 1
        Conference.presentations[conf_name].append(name)
        print("Выберете предложенное свободное время для вашего доклада (в часах): ")
        print(Conference.confs[conf_name])
        chooser = digit_exc()
        c = 0
        while chooser not in Conference.confs[conf_name]:
            c += 1
            if c >= 3:
                print("Извините, вы дебил")
            else:
                print("Извините это время занято, либо выходит за рамки времени конференции")
            print("Введите предложенное выше время для вашего доклада: ")
            chooser = digit_exc()
        self.time = chooser
        if self.time != Conference.confs[conf_name][-1]:
            print("Введите длительность вашего доклада (так, чтобы она не выходила за рамки конференции и свободного времени для докладов): ")
            chooser = digit_exc()
            while (chooser + self.time)-1 not in Conference.confs[conf_name]:
                print("Извините, это время недоступно, введите заново: ")
                chooser = digit_exc()
            self.duration = chooser
        else:
            print("Извините, у вас будет лишь один час")
        for t in range(self.time, self.time + self.duration):
            Conference.confs[conf_name].remove(t)
        Presentation.summary_time += self.duration

class Conference:
    presentations = dict()
    confs = dict()
    def __init__(self,name,begin,end):
        self.confs[name] = [i for i in range(begin,end+1)]
        self.presentations[name] = []
        self.name = name
        # self.presentations[name] = []
    def presents(self):
        for v,k in self.presentations.items():
            print(v,k)

def digit_exc(l=None):
    n = input()
    if l == None:
        while not (str(n).isdigit()):
            print("Вводите символы типа integer")
            n = input()
    else:
        while not (str(n).isdigit()):
            print("Вводите символы типа integer")
            n = input()
        while int(n) not in l:
            print(f"Вводите ТОЛЬКО из элементов {l}")
            n = input()
    return int(n)

conf1 = Conference("Nowadays political problems", 9, 18)
conf2 = Conference("Mathematics in THE REAL WORLD",10,15)
conf3 = Conference("Physics or everything that surrounds us",11,16)
conf4 = Conference("Psychology in school teaching",12,14)

print("Сколько будет докладов: ")
presentation_number = digit_exc()
for i in range(presentation_number):
    print("Выберете конференцию, доклад к которой вы готовили: ")
    for j in range(len(list(Conference.confs.keys()))):
        print(f"{j + 1}) {list(Conference.confs.keys())[j]}")
    chooser = digit_exc()
    conf_name = list(Conference.confs.keys())[chooser - 1]
    theme = input("Введите тему вашего доклада: ")
    speaker = Presentation(theme, conf_name)
chooser = 0
while chooser != 1:
    print("Выберете, что хотите сделать с полученными докладами: \n1)Посмотреть суммарное время докладов\n2)Вывести, сколько в сумме докладов"
          "\n3)Вывести все доклады определённой конференции")
    chooser = digit_exc([1,2,3])
    if chooser == 1: print(f"{Presentation.summary_time} ч")
    elif chooser == 2: print(Presentation.counter)
    else:
        Conference.presentations.keys()
        print("Выберете конференцию, все доклады которой вы хотите увидеть: ")
        for j in range(len(list(Conference.confs.keys()))):
            print(f"{j + 1}) {list(Conference.confs.keys())[j]}")
        chooser = int(input())
        conf_name = list(Conference.confs.keys())[chooser - 1]
        print(Conference.presentations[conf_name])
    print("Ваши следующие действия: \n1) Выход\n2) Вернуться к выбору")
    chooser = digit_exc([1,2])




# speaker1 = Presentation("Nowadays political problems","About society",8,1)
# speaker1.time_fitting(8,2,0)
# speaker1.time_fitting(8,2,0)

# print("Выберете конференцию, доклад к которой вы готовили: ")
# for i in range(len(list(Conference.confs.keys()))):
#     print(f"{i+1}) {list(Conference.confs.keys())[i]}")
# chooser = int(input())
# conf_name = list(Conference.confs.keys())[chooser-1]
#
# print("Выберете предложенное свободное время для вашего доклада (в часах): ")
# print(Conference.confs[conf_name])
# chooser = int(input())
# c = 0
# while chooser not in Conference.confs[conf_name]:
#     c += 1
#     if c >= 3: print("Извините, вы дебил")
#     else: print("Извините это время занято, либо выходит за рамки времени конференции")
#     print("Введите предложенное выше время для вашего доклада: ")
#     chooser = int(input())
# conf_time = chooser
# conf_durence = 1
# if conf_time != Conference.confs[conf_name][-1]:
#     print("Введите длительность вашего доклада (так, чтобы она не выходила за рамки конференции и свободного времени для докладов): ")
#     chooser = int(input())
#     while chooser+conf_time not in Conference.confs[conf_name]:
#         print("Извините, это время недоступно, введите заново: ")
#         chooser = int(input())
#     conf_durence = chooser + conf_time
# else: print("Извините, у вас будет лишь один час")
# print(conf_name,conf_time,conf_durence)

