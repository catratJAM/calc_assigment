import numpy as np
import random


k = 5               # Количество концентраторов
lambda_day = 5      # Интесивность входного потока днем
lambda_night = 0.5  # Интенсивность ночного потока
m = 3               # Максимальный размер очереди
mu = 2.08           # Интенсивность выходного потока
# Количество обслуженных заявок в единицу времени
p_day = lambda_day / mu
p_night = lambda_night / mu

p0 = 0              # Предельная вероятность
f = 1
for i in range(1, k + 1):
    f *= i
    p0 += (p_day ** i) / f
p0 = (p0 + 1 + (((p_day ** (k + 1)) / (k * f)) * (1 - (p_day / k) ** m) / (1 - p_day / k))) ** (-1)
# Вероятность отказа
pd = (p_day ** (k + m) / ((k ** m) * f)) * p0

p0 = 0
f = 1
for i in range(1, k + 1):
    f *= i
    p0 += (p_night ** i) / f
p0 = (p0 + 1 + (((p_night ** (k + 1)) / (k * f)) * (1 - (p_night / k) ** m) / (1 - p_night / k))) ** (-1)
# Вероятность отказа
pe = (p_night ** (k + m) / ((k ** m) * f)) * p0

print('Вероятность отказа днём:', pd)
print('Вероятность отказа ночью:', pe)
