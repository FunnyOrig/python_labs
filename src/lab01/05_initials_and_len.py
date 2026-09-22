FIO = input("ФИО: ")
Initials = FIO.split()
dl = len(Initials[0] + Initials[1] + Initials[2]) + 2
print("Инициалы: " + Initials[0][0] + Initials[1][0] + Initials[2][0] + ".")
print("Длина (символов): " + str(dl))