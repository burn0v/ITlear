attendance = {
    "Робототехника": 0,
    "Футбол": 0,
    "ИЗО": 0,
    "Шахматы": 0
}
def add_key():
    name = input("Введите название кружка: ")
    if name in attendance:
        print('Кружок уже существует')
        return 
    attendance[name] = 0
def set_value():
    name = input("Введите название кружка: ")
    value = int(input("Введите новое значение посещений:"))
    attendance[name] = value
def max_item():
    max_value = max(attendance.values())
    for k, v in attendance.items():
        if v == max_value:
            print("Максимальная посещаемость:",k)
def min_item():
    min_value = min(attendance.values())
    for k, v in attendance.items():
        if v == min_value:
            print("Минимальная посещаемость:",k)
def extra_analysis():
    extra = []
    for k, v in attendance.items():
        if v > 15:
            extra.append(k)
    return extra
        
         
for x in attendance:
    name = x
    value = int(input(f"Введите значение посещенией для {name}:"))
    attendance[name] = value
print("Итого посещений в кружках - ", attendance)
max_item()
min_item()
print("Кружки с посещением больше 15:", extra_analysis())
while True:
    print("1) Показать все кружки")
    print("2) Добавить новый кружок")
    print("3) Обновить посещаемость кружка")
    print("4) Анализ посещаемости")
    print("5) Выйти")

    c = input("Выберите пункт меню: ")
    if c == "1":
        print(attendance)
    elif c == "2":
        add_key()
    elif c == "3":
        set_value()
    elif c == "4":
        max_item()
        min_item()
        print("Кружки с посещением больше 15:", extra_analysis())
    elif c == "5":
        break