# обращаемся к библиотеке numpy и называем np
import numpy as np 

first_range = 1
last_range = 100

# Создаем функцию, которая возвращает результат нашей попытки:если 0, то проходит, 1 - цель больше, 1 - цель меньше
def look (test, butt): 
    if butt < test:
        return(-1)
    if butt > test:
        return(1)
    return(0)


def binar(butt):
	# количество попыток - seek
    seek = 0 
    # ROI (region of interests)
    roi_left = first_range # граница интересов первого числа (слева)
    roi_right = last_range # граница интересов последнего числа (справа)

# цикл для понимания куда двигаться в угадывании
    while roi_left <= roi_right:        
        seek += 1
        middle = int(roi_left + (roi_right - roi_left) / 2)    
        result = look(middle, butt)        
        if result == 0:
            break
        if result == -1: # значит цель меньше, меняем ROI
            roi_right = middle - 1
        if result == 1: # значит цель больше, меняем ROI
            roi_left = middle + 1
            
    return(seek)

# создаем функцию для запуска игры 1000 раз

def run_the_game(game_core_v1):
    '''Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число'''
    listik = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(first_range, last_range + 1, size=(1000))
    for number in random_array:
        listik.append(game_core_v1(number))
    score = int(np.mean(listik))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# запускаем
run_the_game(binar)
