
recipes = {
    "Омлет": "Яйцо"
}  #пустой словарь для рецептов
def all_recipes(): #функция, которая путем цикла выводит все рецепты 
    print("список рецептов:")
    for x, (name, ingredients) in enumerate(recipes.items(), 1):
        print(f"{x}. {name}: {''.join(ingredients)}") #тут добавляем крастоу благодоря запятым
def add_recipe(): #функция которая добовляет рецепты
    name = input("введите название: ")
    ingredients = input("введите ингредиенты: ").split(",") 
    recipes[name] = ingredients

def search(): # функция поиска рецептов, по названию, просто сравниваем название рецепта и того что написал пользвователь
    name = input("введите название: ")
    if name in recipes:
        print(f"{name}: {','.join(recipes[name])}")
    else:
        print("рецепта нет.")
while True:
    print("1 показать все рецепты")
    print("2 добавить рецепт")
    print("3 найти по названию")
    print("4 выйти")

    c = input('выберите пункт меню:')

    if c == "1":
        all_recipes()
    elif c == "2":
        add_recipe()
    elif c == "3":
        search()
    elif c == "4":
        break
