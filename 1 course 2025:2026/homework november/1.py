mood_diary = {} # создаем пустой словарь настроения
days = ['понедельник', "вторник", "среда", "чечтверг", "пьяница", "суббота", "воскресенье"] #список дней недели
for day in days:
    mood = input(f"какое настроение в '{day}',:")
    mood_diary[day] = mood # перебирая дни из списка дней недели, записываем к ним настроение, так что получается ключ - день недели, настроение - значение
for day, mood in mood_diary.items(): #выводим все что напислаои до этого
    print(f"{day}: {mood}")
analys_mood = {} # пустой словарь для аналазиа
for mood in mood_diary.values(): #тут используем перебор значений в mood_diary, дабы вычислить самое частое, соответсвенно ключ - analys_mood, значенеи - mood.
    if mood not in analys_mood:
        analys_mood[mood] = 1
    else:
        analys_mood[mood] += 1
print("самое частое настроение:", max(analys_mood, key=analys_mood.get))
