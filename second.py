import numpy as np
import random
import math
np.random.seed(100)

def task1(k, v, n, bw, m):
    mu = v / n   # Интенсивность выходного потока
    p = bw / n   # Количество обслуженных заявок в единицу времени


def task2(bw, k, mu, m):
    np.random.seed(100)

    n_rep = 50  # Количество повторов в методе Монте-Карло
    p_refuse = 0  # Вероятность блокировки

    n_lost = 0  # Количество потярянных пакетов
    n_packets = 10000

    for i in range(n_rep):
        t = 0                   # Текущее время
        queue = 0               # текущий размер очереди
        t_free = np.zeros(k)    # время, когда прибор освободится

        for f in range(n_packets):
            t += np.random.exponential(scale=1 / bw)  # время поступления нового пакета
            n = 0  # проверяем, есть ли очередь
            if queue > 0:  # если есть
                for j in range(k):
                    while t_free[j] < t and queue > 0:
                        t_free[j] += np.random.exponential(scale=1 / mu)
                        queue -= 1
            for h in range(k):
                if t_free[h] < t:
                    t_free[h] = t + np.random.exponential(scale=1 / mu)
                    break
                else:
                    n += 1
            if n == k:
                if queue < m:
                    queue += 1
                else:
                    n_lost += 1
        p_refuse += n_lost / n_packets   # вероятность отказа: утеряные пакеты/кол-во пакетов

    p_refuse /= n_rep
    return p_refuse


# считается по циклу наращивая очередь
# ( B - 1 ) пока вероятность не станет меньше 0.0001
def task3(k, lambda_, mu):
    n_rep = 100    # Количество повторов в методе Монте-Карло
    # Вероятность блокировки
    p_refuse = 0
    # Имитационное моделирование
    m = 0
    while 1:
        for i in range(n_rep):
            t = 0  # Текущее время
            queue = 0  # текущий размер очереди
            t_free = np.zeros(k)  # время, когда прибор освободится
            n_packets = 10000

            for j in range(k):
                t_free.append(0)
            # Количество потярянных пактеов
            n_lost = 0
            for f in range(n_packets):
                # время поступления нового пакета
                t += np.random.exponential(scale=1 / lambda_)
                # проверяем, свободен ли концентратор
                n = 0
                if queue > 0:
                    for j in range(k):
                        while t_free[j] < t and queue > 0:
                            t_free[j] += np.random.exponential(scale=1 / mu)
                            queue -= 1
                for h in range(k):
                    if t_free[h] < t:
                        t_free[h] = t + np.random.exponential(scale=1 / mu)
                        break
                    else:
                        n += 1
                if n == k:
                    if queue < m:
                        queue += 1
                    else:
                        n_lost += 1
            p_refuse += n_lost / n_packets
        p_refuse /= n_rep
        if p_refuse < 0.0001:
            break
        else:
            m += 1
            p_refuse = 0

    # Оценка вероятности блокировки
    return p_refuse, m + 1


def main():
    k = 5  # Количество концентраторов
    v = 5000  # Скорость передачи
    n = 2400  # Средняя длина пакета
    bw1 = 5  # Интенсивность входного потока днем
    bw2 = 0.5  # Интенсивность входного потока ночью
    buff = 4  # Размер буфера, пакетов

    m = k * (buff - 1)  # Максимальный размер очереди

    p_refuse1 = task2(5, 16 * 3600 * 5)
    p_refuse2 = task2(0.5, 4 * 3600)

    print("Вероятность отказа днём: ", task1(k, v, n, bw1, buff))
    print("Вероятность отказа ночью ", task1(k, v, n, bw2, buff))
    print('Вероятность отказа по методу Монте-Карло днём: ', task2(bw1, k, v / n, m))
    print('Вероятность отказа по методу Монте-Карло ночью: ', task2(bw2, k, v / n, m))
    task3(k, v, n, bw1, buff)


main()