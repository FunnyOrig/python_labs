def format_record(rec: tuple[str, str, float]) -> str:

    if type(rec) != tuple:
        raise TypeError('Запись обязана быть кортежем')
    if len(rec) != 3:
        raise ValueError('Недостаточно данных или перебор')

    fio, group, gpa = rec

    fio = " ".join(fio.strip().split())
    group = " ".join(group.strip().split())

    if not fio:
        raise ValueError("ФИО не может быть пустым")

    if type(fio)!= str or type(group) != str:
       raise TypeError('ФИО и Группа - не строки')

    if not group:
        raise ValueError("Группа не может быть пустой")

    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA должен быть числом")

    if not 0.0 <= gpa <= 5.0:
        raise ValueError("GPA должен быть от 0.0 до 5.0")

    parts = fio.split()

    if len(parts) < 2:
        raise ValueError("ФИО должно содержать хотя бы фамилию и имя")

    if len(parts) > 3:
        raise ValueError("ФИО должно содержать не более трёх частей")

    surname = parts[0].capitalize()

    initials = ""

    for part in parts[1:]:
        initials += part[0].upper() + "."

    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))