# Тут на самом деле сознюсь что делал с использованием гпт, так как не совсем понимал как мне точно написать ту или иную часть кода, поэтому можете не засчитывать, однако я бы просто хотел также посмотреть на мои ошибки если вы их увидели, пожалуйста, напишите и объясните, спасибо!!!!
bd = {}

while True:
    print("1 добавить студента")
    print("2 добавить оценку")
    print("3 показать всех")
    print("4 показать статистику")
    print("5 выход")

    cmd = input("выберите номер ")

    if cmd == "1":
        stu_name = input("имя студента ")
        stu_grades_raw = input("оценки через пробел ").split()

        stu_grades = []
        for g_raw in stu_grades_raw:
            stu_grades.append(float(g_raw))

        bd[stu_name] = stu_grades
        print("добавлен")

    elif cmd == "2":
        who = input("кому добавить оценку ")
        if who in bd:
            new_mark = float(input("оценка "))
            bd[who].append(new_mark)
        else:
            print("нет такого студента")

    elif cmd == "3":
        print("список студентов")
        for stu in bd:
            grades = bd[stu]
            if len(grades) > 0:
                sum_marks = 0
                for mark in grades:
                    sum_marks += mark
                avg_mark = sum_marks / len(grades)
            else:
                avg_mark = 0

            print(stu, avg_mark)

    elif cmd == "4":
        if len(bd) == 0:
            print("нет студентов")
        else:
            best_student = None
            best_avg = -1

            worst_student = None
            worst_avg = 999

            excellent_count = 0

            for stu in bd:
                grades = bd[stu]

                total = 0
                for mark in grades:
                    total += mark

                if len(grades) > 0:
                    avg = total / len(grades)
                else:
                    avg = 0

                if avg > best_avg:
                    best_avg = avg
                    best_student = stu

                if avg < worst_avg:
                    worst_avg = avg
                    worst_student = stu

                if avg >= 4.5:
                    excellent_count += 1

            print("лучший", best_student, best_avg)
            print("худший", worst_student, worst_avg)
            print("отличников", excellent_count)

    elif cmd == "5":
        break

