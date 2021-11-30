import numpy as np
import random



# Количество концентраторов
k_ = 5

# Интенсивность потока
mu_ = 5000 / 2400

lambda_day = 5
lambda_night = 0.5
p_day, b_day = calculations(k_, lambda_day, mu_)
p_night, b_night = calculations(k_, lambda_night, mu_)

print('Вероятность отказа днём: ' + str(p_day))
print('Размер буфера днём: ' + str(b_day))
print('Вероятность отказа ночью: ' + str(p_night))
print('Размер буфера ночью: ' + str(b_night))
