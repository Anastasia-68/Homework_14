
class Counter:
    def __init__(self, current=1, min_value=0, max_value=10):
        # Сохраняем текущее, минимальное и максимальное значения
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        # Устанавливаем начальное значение счётчика
        self.current = start

    def set_max(self, max_max):
        # Устанавливаем максимальное значение счётчика
        self.max_value = max_max

    def set_min(self, min_min):
        # Устанавливаем минимальное значение счётчика
        self.min_value = min_min

    def step_up(self):
        # Если достигли максимума, вызываем исключение
        if self.current >= self.max_value:
            raise ValueError('Достигнут максимум')

        # Увеличиваем значение на единицу
        self.current += 1

    def step_down(self):
        # Если достигли минимума, вызываем исключение
        if self.current <= self.min_value:
            raise ValueError('Достигнут минимум')

        # Уменьшаем значение на единицу
        self.current -= 1

    def get_current(self):
        # Возвращаем текущее значение счётчика
        return self.current


# Создаём счётчик
counter = Counter()

# Проверяем увеличение счётчика
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()

assert counter.get_current() == 10, 'Test1'

try:
    counter.step_up()
except ValueError as e:
    print(e)  # Достигнут максимум

assert counter.get_current() == 10, 'Test2'

# Проверяем уменьшение счётчика
counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()

assert counter.get_current() == 7, 'Test3'

try:
    counter.step_down()
except ValueError as e:
    print(e)  # Достигнут минимум

assert counter.get_current() == 7, 'Test4'
