class Student:
    def __init__(self, name: str, age: int, average_score: float, major: str = "Общая специальность"):
        # Инициализация свойств (используем "приватные" переменные с подчеркиванием)
        self._name = name
        self._age = age
        self._average_score = average_score

        # Дополнительное свойство по усмотрению: Специальность
        self._major = major

        # --- Геттеры и сеттеры ---

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            print("Возраст должен быть положительным числом.")

    @property
    def average_score(self):
        return self._average_score

    @average_score.setter
    def average_score(self, value):
        if 0 <= value <= 10:  # Предполагаем 10-балльную систему
            self._average_score = value
        else:
            print("Средний балл должен быть от 0 до 10.")

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, value):
        self._major = value

    # --- Основные методы ---

    def display_info(self):
        """Выводит информацию о студенте."""
        print(f"Студент: {self._name}, Возраст: {self._age}, Специальность: {self._major}, "
              f"Средний балл: {self._average_score:.1f}")

    def get_performance_evaluation(self):
        """Оценивает успехи студента на основе среднего балла."""
        if self._average_score > 8:
            return "Отлично"
        elif 6 <= self._average_score <= 8:
            return "Хорошо"
        elif 4 <= self._average_score < 6:
            return "Удовлетворительно"
        else:
            return "Неудовлетворительно"

    # --- Дополнительный метод ---

    def have_birthday(self):
        """Дополнительный метод: увеличивает возраст на 1."""
        self._age += 1
        print(f"Поздравляем! {self._name} отпраздновал(а) день рождения. Теперь ему/ей {self._age} лет.")


# ==========================================
# Демонстрация использования класса
# ==========================================
if __name__ == "__main__":
    # 1. Создание нескольких объектов класса "Студент"
    student1 = Student("Александр Иванов", 20, 8.5, "Программная инженерия")
    student2 = Student("Мария Смирнова", 19, 7.2, "Экономика")
    student3 = Student("Иван Петров", 21, 5.0)

    # 2. Вывод информации и оценки успехов
    print("--- Исходная информация ---")
    for student in (student1, student2, student3):
        student.display_info()
        print(f"Оценка успеваемости: {student.get_performance_evaluation()}\n")

    # 3. Использование сеттеров для изменения значений
    print("--- Изменение данных (Студент 3) ---")
    student3.name = "Иван Петров-Водкин"
    student3.average_score = 6.5
    student3.major = "Дизайн"
    student3.display_info()
    print(f"Новая оценка успеваемости: {student3.get_performance_evaluation()}\n")

    # 4. Демонстрация дополнительных методов
    print("--- Вызов дополнительного метода ---")
    student2.have_birthday()