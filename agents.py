import random
from collections import Counter

# Бот 1: Случайный бот
def random_bot(observation, configuration):
    return random.randint(0, 2)

# Бот 2: Только камень
def rock_bot(observation, configuration):
    return 0

# Бот 3: Только ножницы
def scissors_bot(observation, configuration):
    return 2

# Бот 4: Только бумага
def paper_bot(observation, configuration):
    return 1

# Бот 5: Циклический бот (камень -> ножницы -> бумага)
def cycle_bot(observation, configuration):
    if observation.step is None:
        return 0
    else:
        return (observation.step + 1) % 3

# Бот 6: Обратный циклический бот (бумага -> ножницы -> камень)
def reverse_cycle_bot(observation, configuration):
    if observation.step is None:
        return 1
    else:
        return (observation.step + 2) % 3

# Бот 7: Реактивный бот (против последнего хода противника)
def reactive_bot(observation, configuration):
    if observation.step == 0:
        return 0
    else:
        opponent_last_move = observation.lastOpponentAction
        return (opponent_last_move + 1) % 3

# Бот 8: Оппортунист (случайно выбирает ход, побеждающий последний ход противника)
def opportunist_bot(observation, configuration):
    if observation.step == 0:
        return random.randint(0, 2)
    else:
        opponent_last_move = observation.lastOpponentAction
        return (opponent_last_move + 1) % 3

# Бот 9: Против последнего хода с элементом случайности
def counter_random_bot(observation, configuration):
    if observation.step == 0:
        return random.randint(0, 2)
    else:
        opponent_last_move = observation.lastOpponentAction
        # 70% шанс играть против последнего хода, 30% — случайный выбор
        if random.random() < 0.7:
            return (opponent_last_move + 1) % 3
        else:
            return random.randint(0, 2)

# Бот 10: Мстительный бот (повторяет ход, которым противник выиграл)
def revenge_bot(observation, configuration):
    if observation.step == 0 or observation.lastOpponentAction is None:
        return random.randint(0, 2)
    # Если бот проиграл на прошлом шаге, играет победный ход противника
    if observation.reward < 0:
        return observation.lastOpponentAction
    else:
        return random.randint(0, 2)

# Бот 11: Учтивый бот (копирует противника при проигрыше)
def polite_bot(observation, configuration):
    if observation.step == 0:
        return random.randint(0, 2)
    elif observation.reward < 0:  # Копирует ход противника, если проиграл
        return observation.lastOpponentAction
    else:
        return random.randint(0, 2)

# Бот 12: Анализирующий бот (играет против частого хода противника)
def analyzing_bot(observation, configuration):
    if observation.step == 0:
        analyzing_bot.opponent_moves = []
        return random.randint(0, 2)
    
    analyzing_bot.opponent_moves.append(observation.lastOpponentAction)
    most_common_move = Counter(analyzing_bot.opponent_moves).most_common(1)[0][0]
    return (most_common_move + 1) % 3  # Играет против самого частого хода

# Бот 13: Зеркальный бот (повторяет последний ход противника)
def mirror_bot(observation, configuration):
    if observation.step == 0:
        return random.randint(0, 2)
    else:
        return observation.lastOpponentAction

# Бот 14: Наблюдательный бот (играет против самого частого хода противника)
def observing_bot(observation, configuration):
    if observation.step == 0:
        observing_bot.opponent_moves = []
        return random.randint(0, 2)
    
    observing_bot.opponent_moves.append(observation.lastOpponentAction)
    if len(observing_bot.opponent_moves) > 5:  # Проверяет последние 5 ходов
        most_common_move = Counter(observing_bot.opponent_moves[-5:]).most_common(1)[0][0]
    else:
        most_common_move = Counter(observing_bot.opponent_moves).most_common(1)[0][0]
    
    return (most_common_move + 1) % 3  # Играет против самого частого хода