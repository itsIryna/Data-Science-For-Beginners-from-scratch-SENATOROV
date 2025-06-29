"""Classes."""

# ## Классы и объекты в Питоне

# ### Создание класса

# #### Создание класса и метод `.__init__()`

# +
# создадим класс CatClass
# нашему классу понадобится Numpy
# массивом Numpy и другими объектами
# fmt: off
import numpy as np
# из набора линейных моделей библиотеки sklearn импортируем линейную регрессию
from sklearn.linear_model import LinearRegression

# fmt: on


class CatClass:
    """Basic cat class."""

    def __init__(self) -> None:
        """Initialize empty cat instance."""
        pass  # pylint: disable=unnecessary-pass


# -

# #### Создание объекта

# +
# создадим объект Matroskin класса CatClass
Matroskin = CatClass()

# проверим тип данных созданной переменной
type(Matroskin)
# -

# #### Атрибуты класса

# +
# вновь создадим класс CatClass


class CatClass2:
    """Class representing a cat with color and type attributes."""

    def __init__(self, color: str) -> None:
        """Initialize cat with given color."""
        # этот параметр будет записан в переменную атрибута self.color
        self.color: str = color

        # значение атрибута type_ задается внутри класса
        self.type_: str = "cat"


# +
# повторно создадим объект класса CatClass, передав ему параметр цвета шерсти
Matroskin2 = CatClass2("gray")

# и выведем атрибуты класса
print(Matroskin2.color, Matroskin2.type_)
# -

# #### Методы класса

# +
# перепишем класс CatClass


class CatClass3:
    """A class representing a cat with color and type."""

    # метод .__init__() и атрибуты оставим без изменений
    def __init__(self, color: str) -> None:
        """Initialize cat with given color."""
        self.color = color
        self.type_ = "cat"

    # однако добавим метод, который позволит коту мяукать
    def meow(self) -> None:
        """Make the cat meow three times."""
        for _ in range(3):
            print("Мяу")

    # и метод .info() для вывода информации об объекте
    def info(self) -> None:
        """Print the cat's color and type."""
        print(self.color, self.type_)


# -

# создадим объект
Matroskin3 = CatClass3("gray")

# применим метод .meow()
Matroskin3.meow()

# и метод .info()
Matroskin3.info()

# ### Принципы ООП

# #### Инкапсуляция

# +
# изменим атрибут type_ объекта Matroskin на dog
Matroskin3.type_ = "dog"

# выведем этот атрибут
Matroskin3.type_


# -


class CatClass4:
    """A cat with color and type."""

    def __init__(self, color: str) -> None:
        """Initialize cat with color."""
        self.color = color
        # символ подчеркивания ПЕРЕД названием атрибута указывает,
        # что это частный атрибут и изменять его не стоит
        self._type_: str = "cat"


# +
# вновь создадим объект класса CatClass
Matroskin4 = CatClass4("gray")

# и изменим значение атрибута _type_
# Matroskin4._type_ = "dog"
# Matroskin4._type_
# -


class CatClass5:
    """A cat with color and protected type."""

    def __init__(self, color: str) -> None:
        """Initialize cat with color."""
        self.color = color
        # символ двойного подчеркивания предотвратит доступ извне
        # self.__type_: str = "cat"


# при попытке вызова такого атрибута Питон выдаст ошибку
Matroskin5 = CatClass5("gray")
# Matroskin5.__type_

# +
# поставим _CatClass перед __type_
# Matroskin5._CatClass__type_ = "dog"

# к сожалению, значение атрибута изменится
# Matroskin5._CatClass__type_
# -

# #### Наследование классов

# Создание родительского класса и класса-потомка

# +
# создадим класс Animal


class Animal:
    """Animal with weight and length."""

    # пропишем метод .__init__() с двумя параметрами: вес (кг) и длина (см)
    def __init__(self, weight: float, length: float) -> None:
        """Initialize animal with weight and length."""
        # поместим аргументы этих параметров в соответствующие переменные
        self.weight = weight
        self.length = length

    # объявим методы .eat()
    def eat(self) -> None:
        """Make animal eat."""
        print("Eating")

    # и .sleep()
    def sleep(self) -> None:
        """Make animal sleep."""
        print("Sleeping")


# +
# создадим класс Bird
# родительский класс Animal пропишем в скобках


class Bird(Animal):
    """Bird that can fly."""

    # внутри класса Bird объявим новый метод .move()
    def move(self) -> None:
        """Make bird fly."""
        # для птиц .move() будет означать "летать"
        print("Flying")


# -

# создадим объект pigeon и передадим ему значения веса и длины
pigeon = Bird(0.3, 30)

# посмотрим на унаследованные у класса Animal атрибуты
print(pigeon.weight, pigeon.length)

# и методы
pigeon.eat()

# теперь вызовем метод, свойственный только классу Bird
pigeon.move()

# Функция `super()`

# +
# снова создадим класс Bird


class Bird1(Animal):
    """Bird class with flying capability."""

    # в метод .__init__() добавим параметр скорости полета (км/ч)
    def __init__(self, weight: float, length: float, speed: float) -> None:
        """Initialize bird with weight, length and flying speed."""
        # с помощью super() вызовем метод .__init__() род. класса Animal
        super().__init__(weight, length)
        self.flying_speed = speed

    # вновь пропишем метод .move()
    def move(self) -> None:
        """Make bird fly."""
        print("Flying")


# -

# вновь создадим объект pigeon класса Bird, но уже с тремя параметрами
pigeon2 = Bird1(0.3, 30, 100)

# вызовем как унаследованные, так и собственные атрибуты класса Bird
print(pigeon2.weight, pigeon2.length, pigeon2.flying_speed)

# вызовем унаследованный метод .sleep()
pigeon2.sleep()

# и собственный метод .move()
pigeon2.move()

# Переопределение класса

# +
# создадим подкласс Flightless класса Bird


class Flightless(Bird):
    """Flightless bird class that can only run."""

    # метод .__init__() этого подкласса "стирает" .__init__() род. класса
    def __init__(  # pylint: disable=super-init-not-called
        self, running_speed: float
    ) -> None:
        """Initialize flightless bird with running speed."""
        # таким образом, у нас остается только один атрибут
        self.running_speed = running_speed

    # кроме того, результатом метода .move() будет 'Running'
    def move(self) -> None:
        """Make flightless bird run."""
        print("Running")


# -

# создадим объект ostrich класса Flightless
ostrich = Flightless(60)

# посмотрим на значение атрбута скорости
print(ostrich.running_speed)

# и проверим метод .move()
ostrich.move()

# подкласс Flightless сохранил методы всех родительских классов
ostrich.eat()

# Множественное наследование

# +
# создадим родительский класс Fish


class Fish:
    """Base class for fish that can swim."""

    # и метод .swim()
    def swim(self) -> None:
        """Make fish swim."""
        print("Swimming")


# +
# и еще один родительский класс Bird


class Bird2:
    """Base class for birds that can fly."""

    # и метод .fly()
    def fly(self) -> None:
        """Make bird fly."""
        print("Flying")


# +
# теперь создадим класс-потомок этих двух классов


class SwimmingBird(Bird2, Fish):
    """A bird that can both swim and fly."""

    pass  # pylint: disable=unnecessary-pass


# -

# создадим объект duck класса SwimmingBird
duck = SwimmingBird()

# как мы видим утка умеет как летать,
duck.fly()

# так и плавать
duck.swim()

# #### Полиморфизм

# для чисел '+' является оператором сложения
print(2 + 2)

# для строк - оператором объединения
print("классы" + " и " + "объекты")

# 1. Полиморфизм функций

# функцию len() можно применить к строке
len("Программирование на Питоне")

# кроме того, она способна работать со списком
len(["Программирование", "на", "Питоне"])

# словарем
len({0: "Программирование", 1: "на", 2: "Питоне"})

len(np.array([1, 2, 3]))

# 2. Полиморфизм классов

# Создадим объекты с одинаковыми атрибутами и методами

# +
# создадим класс котов


class CatClass6:
    """Class representing a cat with name, type and color attributes."""

    # определим атрибуты клички, типа и цвета шерсти
    def __init__(self, name: str, color: str) -> None:
        """Initialize a cat with given name and color."""
        self.name = name
        self._type_ = "кот"
        self.color = color

    # создадим метод .info() для вывода этих атрибутов
    def info(self) -> None:
        """Print information about the cat."""
        print(f"Меня зовут {self.name}, я {self._type_}")
        print(f"цвет моей шерсти {self.color}")

    # и метод .sound(), показывающий, что коты умеют мяукать
    def sound(self) -> None:
        """Print the sound a cat makes."""
        print("Я умею мяукать")


# +
# создадим класс собак


class DogClass:
    """Class representing a dog with name, type and color attributes."""

    # с такими же атрибутами
    def __init__(self, name: str, color: str) -> None:
        """Initialize a dog with given name and color."""
        self.name = name
        self._type_ = "пес"
        self.color = color

    # и методами
    def info(self) -> None:
        """Print information about the dog."""
        print(f"Меня зовут {self.name}, я {self._type_}")
        print(f"цвет моей шерсти {self.color}")

    # хотя, обратите внимание, действия внутри методов отличаются
    def sound(self) -> None:
        """Print the sound a dog makes."""
        print("Я умею лаять")


# -

# Создадим объекты этих классов

cat = CatClass6("Бегемот", "черный")
dog = DogClass("Барбос", "серый")

# В цикле `for` вызовем атрибуты и методы каждого из классов

for animal in (cat, dog):
    animal.info()
    animal.sound()
    print()

# ### Парадигмы программирования

patients: list[dict[str, str | int]] = [
    {"name": "Николай", "height": 178},
    {"name": "Иван", "height": 182},
    {"name": "Алексей", "height": 190},
]

# #### Процедурное программирование

# +
# создадим переменные для общего роста и количества пациентов
total, count = 0, 0

# в цикле for пройдемся по пациентам (отдельным словарям)
for patient in patients:
    # достанем значение роста и прибавим к текущему значению переменной total
    total += int(patient["height"])
    # на каждой итерации будем увеличивать счетчик пациентов на один
    count += 1

# разделим общий рост на количество пациентов,
# чтобы получить среднее значение
print(total / count)
# -

# #### Объектно-ориентированное программирование

# +
# создадим класс для работы с данными DataClass


class DataClass:
    """Class for calculating statistics on data."""

    # при создании объекта будем передавать ему данные для анализа
    def __init__(self, data: list[dict[str, str | int]]) -> None:
        """Initialize with data for analysis."""
        self.data = data
        self.metric = ""
        self.__total = 0
        self.__count = 0

    # кроме того, создадим метод для расчета среднего значения
    def count_average(self, metric: str) -> float:
        """Calculate average value for given metric."""
        # параметр metric определит, по какому столбцу считать среднее
        self.metric = metric

        # объявим два частных атрибута
        self.__total = 0
        self.__count = 0

        # в цикле for пройдемся по списку словарей
        for item in self.data:

            # рассчитем общую сумму по указанному в metric
            # значению каждого словаря
            self.__total += int(item[self.metric])

            # и количество таких записей
            self.__count += 1

        # разделим общую сумму показателя на количество записей
        return self.__total / self.__count


# +
# создадим объект класса DataClass и передадим ему данные о пациентах
data_object = DataClass(patients)

# вызовем метод .count_average() с метрикой 'height'
data_object.count_average("height")
# -

# #### Функциональное программирование

# Функция map()

# lambda-функция достанет значение по ключу height
# функция map() применит lambda-функцию к каждому вложенному в patients словарю
# функция list() преобразует результат в список
heights = list(map(lambda x: int(x["height"]), patients))
print(heights)

# воспользуемся функциями sum() и len() для нахождения среднего значения
print(sum(heights) / len(heights))

# Функция einsum()

# +
# возьмем два двумерных массива
a_val = np.array([[0, 1, 2], [3, 4, 5]])

b_val = np.array([[5, 4], [3, 2], [1, 0]])
# -

# перемножим a и b по индексу j через функцию np.einsum()
np.einsum("ij, jk -> ik", a_val, b_val)

# ### Классы и объекты в машинном обучении

# #### Готовые классы в библиотеке sklearn

# возьмем данные роста и обхвата шеи
x_val_ar = np.array(
    [
        1.48,
        1.49,
        1.49,
        1.50,
        1.51,
        1.52,
        1.52,
        1.53,
        1.53,
        1.54,
        1.55,
        1.56,
        1.57,
        1.57,
        1.58,
        1.58,
        1.59,
        1.60,
        1.61,
        1.62,
        1.63,
        1.64,
        1.65,
        1.65,
        1.66,
        1.67,
        1.67,
        1.68,
        1.68,
        1.69,
        1.70,
        1.70,
        1.71,
        1.71,
        1.71,
        1.74,
        1.75,
        1.76,
        1.77,
        1.77,
        1.78,
    ]
)
y_val_ar = np.array(
    [
        29.1,
        30.0,
        30.1,
        30.2,
        30.4,
        30.6,
        30.8,
        30.9,
        31.0,
        30.6,
        30.7,
        30.9,
        31.0,
        31.2,
        31.3,
        32.0,
        31.4,
        31.9,
        32.4,
        32.8,
        32.8,
        33.3,
        33.6,
        33.0,
        33.9,
        33.8,
        35.0,
        34.5,
        34.7,
        34.6,
        34.2,
        34.8,
        35.5,
        36.0,
        36.2,
        36.3,
        36.6,
        36.8,
        36.8,
        37.0,
        38.5,
    ]
)

# преобразуем данные роста в двумерный массив
X_2D = x_val_ar.reshape(-1, 1)
print(X_2D)

# +
# создадим объект этого класса и запишем в переменную model
model = LinearRegression()

# обучим модель с помощью метода .fit(), которому передадим наши данные
model.fit(X_2D, y_val_ar)

# на выходе получим коэффициенты линейной регрессии
print(model.coef_, model.intercept_)
# -

# построим прогноз и выведем первые пять значений
y_pred = model.predict(X_2D)
print(y_pred[:5])

# #### Пример ООП: собственный класс линейной регрессии

# +
# создадим класс SimpleLinearRegression


class SimpleLinearRegression:
    """Simple implementation of linear regression."""

    # в методе .__init__() объявим переменные наклона и сдвига
    def __init__(self) -> None:
        """Initialize model coefficients."""
        self.slope_ = 0.0
        self.intercept_ = 0.0

    # создадим метод .fit()
    def fit(self, x_val, y_val) -> None:  # type: ignore
        """Fit linear regression model."""
        # найдем среднее значение X и y
        x_mean = self.find_mean(x_val)
        y_mean = self.find_mean(y_val)

        # объявим переменные для числителя и знаменателя
        numerator, denominator = 0, 0

        # в цикле пройдемся по данным
        for index, x_el in enumerate(x_val):
            y_el = y_val[index]

            # вычислим значения числителя и знаменателя по формуле выше
            numerator += (x_el - x_mean) * (y_el - y_mean)
            denominator += (x_el - x_mean) ** 2

        # найдем наклон и сдвиг
        slope_ = numerator / denominator
        intercept_ = y_mean - slope_ * x_mean

        # сохраним получившиеся коэффициенты в виде атрибутов
        self.slope_ = slope_
        self.intercept_ = intercept_

    # метод .predict() просто умножит через скалярное произведение
    # вектор данных на наклон и прибавит сдвиг
    def predict(self, x_val: np.ndarray):  # type: ignore
        """Make predictions using fitted model."""
        # на выходе мы получим вектор прогнозных значений
        return np.dot(self.slope_, x_val) + self.intercept_

    # служебный метод: расчет среднего
    def find_mean(self, nums: np.ndarray):  # type: ignore
        """Calculate mean of input numbers."""
        return sum(nums) / len(nums)


# -

# создадим объект класса SimpleLinearRegression
model = SimpleLinearRegression()

# +
# применим метод .fit()
model.fit(x_val_ar, y_val_ar)

# посмотрим на коэффициенты
print(model.slope_, model.intercept_)

# +
# сделаем прогноз через .predict()
y_pred = model.predict(x_val_ar)

# и выведем первые пять коэффициентов
print(y_pred[:5])