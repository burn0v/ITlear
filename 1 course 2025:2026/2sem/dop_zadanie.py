import random
import time
import matplotlib.pyplot as plt

def insertion_sort(mas):
    for i in range(1, len(mas)):
        key = mas[i]
        j = i - 1
        while j >= 0 and key < mas[j]:
            mas[j + 1] = mas[j]
            j -= 1
        mas[j + 1] = key

sizes = [100, 250, 500, 1000, 2000]
times = []

for n in sizes:
    sum_time = 0
    
    for _ in range(30):
        arr = []
        for i in range(n):
            arr.append(random.randint(1, 1000))
            
        start = time.time()
        insertion_sort(arr)
        end = time.time()
        
        sum_time += (end - start)
        
    srednee = sum_time / 30
    times.append(srednee)
    print("Размер:", n, "Среднее время:", srednee)

plt.plot(sizes, times, marker='o')
plt.title('Сортировка вставками')
plt.xlabel('Размер массива')
plt.ylabel('Время (сек)')
plt.grid()
plt.show()