from typing import Union
import doctest


# TODO Написать 3 класса с документацией и аннотацией типов
class Place:
    """
    Documentation on the class.
    This class describes a model of a geographical place.

    >>> place = Place("some_name", (60.007218, 30.373016))
    >>> place.visit()
    You have visited the some_name and enjoyed it.
    >>> place.rename("place")
    >>> print(place.name)
    place
    """
    def __init__(self, name: str, coordinates: tuple[float, float]):
        """
        Initialization of instance.
        :param name: The name of the place.
        :param coordinates: Its position represented by a latitude-longitude pair.
        """
        if not isinstance(name, str):
            raise TypeError("The name should be a string.")
        if not isinstance(coordinates, tuple):
            raise TypeError("Coordinates should be represented by a tuple.")
        if (not isinstance(coordinates[0], (float, int))) or (not isinstance(coordinates[1], (float, int))):
            raise TypeError("Coordinates should consist of two numbers.")
        if (coordinates[0] > 90.0) or (coordinates[0] < -90.0):
            raise ValueError("Latitude should be in bounds [-90; 90].")
        if (coordinates[1] > 180.0) or (coordinates[1] < -180.0):
            raise ValueError("Longitude should be in bounds [-180; 180].")

        self.name = name
        self.coordinates = coordinates

    def visit(self) -> None:
        """
        You can visit a place.
        There is no return.
        """
        print(f"You have visited the {self.name} and enjoyed it.")

    def rename(self, new_name) -> None:
        """
        This method renames the place.

        :param new_name: New name, should be a string.
        There is no return.
        """
        if not isinstance(new_name, str):
            raise TypeError("The name should be a string.")
        self.name = new_name


class Tree:
    """
    Documentation on the class.
    This class describes a model of a tree.
    """
    def __init__(self, height: Union[int, float], specie="Oak"):
        """
        Initializes the instance.
        :param height: Height of your tree.
        :param specie: Specie of your tree, represented by a string.
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Height should be a number.")
        if not isinstance(specie, str):
            raise TypeError("Specie should be given by a string.")
        if height <= 0:
            raise ValueError("Height should be a positive number.")

        self.height = height
        self.specie = specie

    def grow(self, dh: Union[int, float]) -> None:
        """
        This method grows your tree by dh.
        :param dh: Height increment. Can be non-positive but the resulting height should be positive.
        No return.

        >>> tree = Tree(15, "Birch")
        >>> print(tree.height)
        15
        >>> tree.grow(-5)
        >>> print(tree.height)
        10
        """
        if not isinstance(dh, (int, float)):
            raise TypeError("Height increment should be a number.")
        if self.height + dh <= 0:
            raise ValueError("Resulting height seems to be non-positive.")

        self.height += dh

    def wind(self) -> None:
        """
        This method makes tree noise in the wind.
        No return.

        >>> tree = Tree(20, "Spruce")
        >>> tree.wind()
        shhhh
        """
        print("shhhh")

class Alexander_Nikolayevich:
    """
    Documentation on the class.
    This class describes a model of the higher maths teacher.
    """
    def __init__(self, mood: str, dopsa=True):
        """
        Initializes the instance.
        :param mood: Can have only two values: "Neutral" and "Furious".
        :param dopsa: Must be boolean.
        """
        if not isinstance(mood, str):
            raise TypeError("Mood should be represented by a string.")
        if not isinstance(dopsa, bool):
            raise TypeError("Dopsa should be represented by a boolean value.")
        if mood not in ["Neutral", "Furious"]:
            raise ValueError("Mood could only be Neutral or Furious.")

        self.mood = mood
        self.dopsa = dopsa

    def practice(self) -> None:
        """
        Makes the sound of practice. After that makes the teacher furious.
        No return.

        >>> prepod = Alexander_Nikolayevich("Neutral")
        >>> prepod.practice()
        Есть вопросы по домашнему заданию?
        >>> print(prepod.mood)
        Furious
        """
        print("Есть вопросы по домашнему заданию?")
        self.mood = "Furious"

    def exam(self, is_student_clever=False) -> None:
        """
        Models Alexander Nikolayevich's exam.
        :param is_student_clever: Defines if the student clever or not.
        No return.

        >>> prepod = Alexander_Nikolayevich("Neutral")
        >>> prepod.exam(True)
        Оценка 3. Подтвердите своё согласие с ней.
        >>> print(prepod.dopsa, prepod.mood)
        False Neutral
        """
        if not isinstance(is_student_clever, bool):
            raise TypeError("is_student_clever should have boolean value.")
        if not is_student_clever:
            print("Вы вообще ничего не знаете! Отправляйтесь на пересдачу, у вас будет время подготовиться к ней.")
            self.dopsa = True
            self.mood = "Furious"
        else:
            print("Оценка 3. Подтвердите своё согласие с ней.")
            self.dopsa = False
            self.mood = "Neutral"

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
