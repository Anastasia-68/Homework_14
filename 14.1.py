
class Human:
    def __init__(self, gender, age, first_name, last_name):
        # Сохраняем информацию о человеке
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        # Возвращаем информацию о человеке в виде строки
        return f'{self.first_name} {self.last_name}, {self.age} years old, {self.gender}'


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        # Вызываем конструктор родительского класса Human
        super().__init__(gender, age, first_name, last_name)

        # Добавляем свойство, которое есть только у студента
        self.record_book = record_book

    def __str__(self):
        # Переопределяем метод и добавляем номер зачётной книжки
        return f'{self.first_name} {self.last_name}, {self.age} years old, {self.gender}, record book: {self.record_book}'


class Group:
    def __init__(self, number):
        self.number = number
        # Множество для хранения студентов
        self.group = set()

    def add_student(self, student):
        # Добавляем студента в группу
        self.group.add(student)

    def find_student(self, last_name):
        # Ищем студента по фамилии
        for student in self.group:
            if student.last_name == last_name:
                # Возвращаем сам объект студента
                return student

        # Если студент не найден
        return None

    def delete_student(self, last_name):
        # Сначала ищем студента по фамилии
        student = self.find_student(last_name)

        # Удаляем только в том случае, если студент найден
        if student is not None:
            self.group.remove(student)

    def __str__(self):
        # Собираем информацию обо всех студентах группы
        all_students = ''

        for student in self.group:
            all_students += str(student) + '\n'

        return f'Number:{self.number}\n {all_students}'


# Создаём студентов
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

# Создаём группу
gr = Group('PD1')

# Добавляем студентов в группу
gr.add_student(st1)
gr.add_student(st2)

# Выводим информацию о группе
print(gr)

# Проверяем работу поиска
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр'

# Удаляем студента
gr.delete_student('Taylor')
print(gr)  # В группе остался один студент

# Повторное удаление не вызывает ошибку
gr.delete_student('Taylor')
