records = {
    "Барсик": ["кот", 3, 4],
    "Шарик": ["пёс", 5, 12]
}
def add_record(records):
    name_pet = input("Введите имя питомца:")
    type_pet = input("Введите вид питомца:")
    age_pet = int(input("Введите возраст питомца:"))
    weight_pet = int(input("Введите вес питомца:"))
    if name_pet in records:
        print('Питомец уже добавлен')
        return 
    records[name_pet] = [type_pet, age_pet, weight_pet]
def show_all(records):
    for name, data in records.items():
         print(f"{name}: {data}")
def find_record(records):
    name_pet = input("Введите имя для поиска: ")
    if name_pet in records:
        print(f"{name_pet}, {records[name_pet]}")
def extra_feature(records):
    x = int(input("Показать животных старше какого возраста? "))
    print(f"Животные старше {x} лет")
    for name, data in records.items():
        if data[1] > x:
            print(f"{name}: {data}")
while True:
    print("1 — Показать всех животных")
    print("2 — Добавить животное")
    print("3 — Найти животное по имени")
    print("4 — Показать животных старше X лет")
    print("5 — Выйти")

    c = input("Выберите пункт: ")

    if c == "1":
        show_all(records)
    elif c == "2":
        add_record(records)
    elif c == "3":
        find_record(records)
    elif c == "4":
        extra_feature(records)
    elif c == "5":
        break